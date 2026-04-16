import re
from datetime import datetime
from typing import Tuple
 
 
def calculate_vat(price: float, rate: float = 0.15) -> float:
    """Calculate the VAT amount for a given price.
 
    Args:
        price: The price before VAT. Must be a non-negative number.
        rate: The VAT rate as a decimal. Default is 0.15 for 15%.
 
    Returns:
        The VAT amount for the provided price.
 
    Raises:
        ValueError: If price is negative or rate is outside 0 to 1.
 
    Example:
        >>> calculate_vat(100)
        15.0
    """
    if not isinstance(price, (int, float)):
        raise ValueError("Price must be a number.")
    if not isinstance(rate, (int, float)):
        raise ValueError("Rate must be a number.")
    if price < 0:
        raise ValueError("Price cannot be negative.")
    if rate < 0 or rate > 1:
        raise ValueError("Rate must be between 0 and 1.")
 
    return float(price * rate)
 
 
def sa_tax_bracket(annual_income: float) -> str:
    """Return the SARS tax bracket and rate for South African annual income.
 
    Args:
        annual_income: The annual income amount. Must be a non-negative number.
 
    Returns:
        A string describing the tax bracket and the applicable rate.
 
    Raises:
        ValueError: If annual_income is negative or not a number.
 
    Example:
        >>> sa_tax_bracket(250000)
        '23% (R237101 - R370500)'
    """
    if not isinstance(annual_income, (int, float)):
        raise ValueError("Annual income must be a number.")
    if annual_income < 0:
        raise ValueError("Annual income cannot be negative.")
 
    brackets = [
        (0, 237100, "18% (R0 - R237100)"),
        (237101, 370500, "23% (R237101 - R370500)"),
        (370501, 512800, "26% (R370501 - R512800)"),
        (512801, 673000, "31% (R512801 - R673000)"),
        (673001, 857900, "36% (R673001 - R857900)"),
        (857901, 1817000, "39% (R857901 - R1 817 000)"),
        (1817001, float("inf"), "45% (R1 817 001 and above)"),
    ]
 
    for lower, upper, description in brackets:
        if lower <= annual_income <= upper:
            return description
 
    raise ValueError("Unable to determine tax bracket.")
 
 
def validate_sa_id(id_number: str) -> bool:
    """Validate a South African ID number.
 
    Args:
        id_number: The ID number string to validate. Must contain 13 digits.
 
    Returns:
        True if the ID number is valid, otherwise False.
 
    Example:
        >>> validate_sa_id('8001015009087')
        True
    """
    if not isinstance(id_number, str):
        raise ValueError("ID number must be provided as a string.")
 
    if not re.fullmatch(r"\d{13}", id_number):
        return False
 
    dob = id_number[:6]
    try:
        year = int(dob[0:2])
        month = int(dob[2:4])
        day = int(dob[4:6])
 
        # Decide century for birth year using 100-year window.
        current_year = datetime.now().year % 100
        base_century = 1900 if year > current_year else 2000
        full_year = base_century + year
 
        datetime(full_year, month, day)
    except ValueError:
        return False
 
    return True
 
 
def convert_km_to_miles(km: float) -> float:
    """Convert kilometres to miles using the conversion factor 1 km = 0.621371 miles.
 
    Args:
        km: Distance in kilometres. Must be a non-negative number.
 
    Returns:
        Distance in miles.
 
    Raises:
        ValueError: If km is negative or not a number.
 
    Example:
        >>> convert_km_to_miles(10)
        6.21371
    """
    if not isinstance(km, (int, float)):
        raise ValueError("Kilometres must be a number.")
    if km < 0:
        raise ValueError("Kilometres cannot be negative.")
 
    return float(km * 0.621371)
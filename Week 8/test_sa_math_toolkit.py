import pytest
from sa_math_toolkit import calculate_vat, sa_tax_bracket, validate_sa_id, convert_km_to_miles
 
 
def test_calculate_vat_normal_case():
    assert calculate_vat(100) == 15.0
 
 
def test_calculate_vat_custom_rate():
    assert calculate_vat(200, rate=0.2) == 40.0
 
 
def test_calculate_vat_invalid_price():
    with pytest.raises(ValueError):
        calculate_vat(-50)
 
 
def test_sa_tax_bracket_lower_boundary():
    assert sa_tax_bracket(100000) == "18% (R0 - R237100)"
 
 
def test_sa_tax_bracket_middle_bracket():
    assert sa_tax_bracket(300000) == "23% (R237101 - R370500)"
 
 
def test_sa_tax_bracket_invalid_income():
    with pytest.raises(ValueError):
        sa_tax_bracket(-1000)
 
 
def test_validate_sa_id_valid():
    assert validate_sa_id("8001015009087") is True
 
 
def test_validate_sa_id_invalid_format():
    assert validate_sa_id("123456789012") is False
 
 
def test_validate_sa_id_invalid_date():
    assert validate_sa_id("9902315009087") is False
 
 
def test_convert_km_to_miles_normal_case():
    assert convert_km_to_miles(10) == pytest.approx(6.21371)
 
 
def test_convert_km_to_miles_zero():
    assert convert_km_to_miles(0) == 0.0
 
 
def test_convert_km_to_miles_invalid():
    with pytest.raises(ValueError):
        convert_km_to_miles(-5)
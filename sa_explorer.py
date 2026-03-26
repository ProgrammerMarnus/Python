print("=== Welcome to SA Explorer! ===")
print("Provinces: Gauteng, Western Cape, KwaZulu-Natal, Eastern Cape, Free State, Limpopo, Mpumalanga, Northern Cape, North West")
print()

choice = input("What province do you want to explore? ").strip().lower()
print()

if choice == "gauteng":
    capital = "Johannesburg"
    population = "~15 million"
    area = "18,178 km²"
    languages = "isiZulu, English, Afrikaans, Sesotho"
    print(f"=== Gauteng ===")
    print(f"{'Capital:':15} {capital}")
    print(f"{'Population:':15} {population}")
    print(f"{'Area:':15} {area}")
    print(f"{'Languages:':15} {languages}")

elif choice == "western cape":
    capital = "Cape Town"
    population = "~7 million"
    area = "129,462 km²"
    languages = "Afrikaans, isiXhosa, English"
    print(f"=== Western Cape ===")
    print(f"{'Capital:':15} {capital}")
    print(f"{'Population:':15} {population}")
    print(f"{'Area:':15} {area}")
    print(f"{'Languages:':15} {languages}")

elif choice == "kwazulu-natal":
    capital = "Pietermaritzburg"
    population = "~11 million"
    area = "94,361 km²"
    languages = "isiZulu, English"
    print(f"=== KwaZulu-Natal ===")
    print(f"{'Capital:':15} {capital}")
    print(f"{'Population:':15} {population}")
    print(f"{'Area:':15} {area}")
    print(f"{'Languages:':15} {languages}")

elif choice == "eastern cape":
    capital = "Bhisho"
    population = "~7 million"
    area = "168,966 km²"
    languages = "isiXhosa, Afrikaans, English"
    print(f"=== Eastern Cape ===")
    print(f"{'Capital:':15} {capital}")
    print(f"{'Population:':15} {population}")
    print(f"{'Area:':15} {area}")
    print(f"{'Languages:':15} {languages}")

elif choice == "free state":
    capital = "Bloemfontein"
    population = "~3 million"
    area = "129,825 km²"
    languages = "Sesotho, Afrikaans, English"
    print(f"=== Free State ===")
    print(f"{'Capital:':15} {capital}")
    print(f"{'Population:':15} {population}")
    print(f"{'Area:':15} {area}")
    print(f"{'Languages:':15} {languages}")

elif choice == "limpopo":
    capital = "Polokwane"
    population = "~6 million"
    area = "125,755 km²"
    languages = "Sepedi, Tshivenda, Xitsonga"
    print(f"=== Limpopo ===")
    print(f"{'Capital:':15} {capital}")
    print(f"{'Population:':15} {population}")
    print(f"{'Area:':15} {area}")
    print(f"{'Languages:':15} {languages}")

elif choice == "mpumalanga":
    capital = "Mbombela (Nelspruit)"
    population = "~4.5 million"
    area = "76,495 km²"
    languages = "isiZulu, siSwati, English"
    print(f"=== Mpumalanga ===")
    print(f"{'Capital:':15} {capital}")
    print(f"{'Population:':15} {population}")
    print(f"{'Area:':15} {area}")
    print(f"{'Languages:':15} {languages}")

elif choice == "northern cape":
    capital = "Kimberley"
    population = "~1.3 million"
    area = "372,889 km²"
    languages = "Afrikaans, Setswana, isiXhosa"
    print(f"=== Northern Cape ===")
    print(f"{'Capital:':15} {capital}")
    print(f"{'Population:':15} {population}")
    print(f"{'Area:':15} {area}")
    print(f"{'Languages:':15} {languages}")

elif choice == "north west":
    capital = "Mahikeng"
    population = "~4 million"
    area = "104,882 km²"
    languages = "Setswana, Afrikaans, English"
    print(f"=== North West ===")
    print(f"{'Capital:':15} {capital}")
    print(f"{'Population:':15} {population}")
    print(f"{'Area:':15} {area}")
    print(f"{'Languages:':15} {languages}")

else:
    print(f"Sorry, province not found.")

print()

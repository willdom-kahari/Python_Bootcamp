# Define variables and get user input
names = input("Enter 5 names of people (separated by a comma): ").title().split(",")
names = list(map(str.strip, names))

ages = input("Enter the corresponding age of each person (separated by a comma): ").split(",")
ages = list(map(int, map(str.strip,ages)))

countries = input("Enter the corresponding country of each person (separated by a comma): ").title().split(",")
countries = list(map(str.strip, countries))

allowed_countries = ("Kenya", "Nigeria", "South Africa")

# Validate input to ensure there are 5 records
if (len(names) != 5) or (len(ages) != 5) or (len(countries) != 5):
    print("The number of people, ages and countries must each be 5 (separated by a comma).")
    exit()
else:
    # Counter variable
    number_of_people_from_allowed_countries = 0

    # Check if the last country is in the whitelist
    if countries[4] in allowed_countries:
        print(f"{names[4]} is from an allowed country")
    else:
        print(f"{names[4]} is not from an allowed country")

    # Check the number of people in allowed countries
    if allowed_countries[0] in countries:
        number_of_people_from_allowed_countries += 1
    if allowed_countries[1] in countries:
        number_of_people_from_allowed_countries += 1
    if allowed_countries[2] in countries:
        number_of_people_from_allowed_countries += 1

    #print results
    print(f"Total number of people checked: {len(names)}")
    print(f"Number of people from allowed countries: {number_of_people_from_allowed_countries}")
    print(f"Number of people not from allowed countries: {len(names) - number_of_people_from_allowed_countries}")

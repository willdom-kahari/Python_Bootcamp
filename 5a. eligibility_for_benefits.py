#1. Define variable age, is_student, and is_employed
age = int(input("Enter your age: "))
is_student= input("Are you a student? Yes or No: ").capitalize()
is_employed = input("Are you employed? Yes or No: ").capitalize()

#2. Using logical operators (and, or) determine eligibility for different benefits
if is_student == "Yes" and age < 25:
    print("Eligible for student discount.")
elif is_employed == "Yes" and 18 < age < 65:
    print("Eligible for work benefits.")
elif is_student == "Yes" or is_employed == "Yes":
    print("Eligible for general benefits.")
else:
    print("Not eligible for general benefits.")


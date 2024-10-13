# 1. Define variable
age = int(input("Enter your age: "))

if age < 0: print("Age Cannot be less than 0.")
elif 0 <= age <= 12: print("You are a child")
elif 12 <= age <= 19: print("You are a teenager")
elif 19 <= age <= 64: print("You are an adult")
else: print("You are old")


# if age >= 65:
#     print("You are old")
# elif age >=20:
#     print("You are an adult")
# elif age >=13:
#     print("You are a teenager")
# elif age >=0:
#     print("You are a child")
# else:
#     print("Age cannot be less than zero.")
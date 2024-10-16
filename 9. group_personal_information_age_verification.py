#1. Declare variables
names = []
ages = []
age_threshold = 18

print("============================================================")
print("WELCOME TO THE PERSONAL INFORMATION AGE VERIFICATION SYSTEM.")
print("============================================================\n")

# Input values
for counter in range(5):
    name = input(f"Enter name {counter+1}: ").strip().title()
    age = int(input(f"Enter {name}'s age: "))
    names.append(name)
    ages.append(age)
    print("============================================================")

#2. Iterate over the names
for name in names:
    position = names.index(name)

    if ages[position] >= age_threshold:
        print(f"{name} is eligible")
    else:
        print(f"{name} is not eligible")


#3. Process names
print("============================================================")
for name in names:
    print(f"Processing {name}...")
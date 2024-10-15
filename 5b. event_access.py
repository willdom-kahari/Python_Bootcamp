# 1. Define variables age, is_member, and has_invitation
age = int(input("Enter your age:"))
is_member = input("Are you a member of this club? Yes or No: ").strip().capitalize() == "Yes"
has_invitation = input("Do you have an invitation? Yes or No: ").strip().capitalize() == "Yes"

# 2. Using logical operators (and, or), determine access to different events
if is_member and age >= 18:
    print("Access to Member's Event.")
elif is_member and has_invitation:
    print("Access to Exclusive Event.")
elif has_invitation or age >= 21:
    print("Access to VIP Event.")
else:
    print("Access to General Event.")
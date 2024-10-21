import random

secret_number = random.randint(1, 10)
user_number = int(input("Enter a number between 1 and 10: "))

if user_number == secret_number:
    print(f"You win! {secret_number} is the secret number.")
else:
    print(f"You lose! {secret_number} is the secret number.")
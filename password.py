import random

print("PASSWORD GENERATOR")

small_letters = "abcdefghijklmnopqrstuvwxyz"
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

all_characters = small_letters + capital_letters + numbers + symbols

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password = password + random.choice(all_characters)

print("\nGenerated Password:")
print(password)

again = input("\nGenerate another password? (yes/no): ")

while again.lower() == "yes":

    length = int(input("Enter password length: "))

    password = ""

    for i in range(length):
        password = password + random.choice(all_characters)

    print("\nGenerated Password:")
    print(password)

    again = input("\nGenerate another password? (yes/no): ")

print("Program Ended")
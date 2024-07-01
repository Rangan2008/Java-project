import string
import random

def generate_password(length):
    if length>8:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password
    else:
        print("Please enter length ")
length = int(input("Enter the desired password length: "))

# Generate the password
password = generate_password(length)

# Print the generated password
print(f"Generated password: {password}")

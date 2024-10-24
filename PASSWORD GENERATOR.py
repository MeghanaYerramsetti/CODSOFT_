import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1."

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + punctuation

    # Ensure the password has at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(punctuation)
    ]

    # Fill the rest of the password length
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the result to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Welcome to the Password Ge

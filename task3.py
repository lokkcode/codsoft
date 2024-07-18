import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the length of password: "))
    password = generate_password(length)
    print("Generated password:", password)

if __name__ == "__main__":
    main()
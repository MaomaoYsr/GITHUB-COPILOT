def main():
    print("welcome to the password generator")
    while True:
        print("\n1. Generate a password\n2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            password = generate_password()
            print(f"Your password is: {password}")
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

def generate_password():
    import random
    import string
    length = int(input("Enter the length of the password: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    main()
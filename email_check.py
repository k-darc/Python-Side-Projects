import re

def valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def main():
    while True:
        email = input("Enter your email: ")

        if not email.strip():
            print("Invalid Email")
            continue

        if valid_email(email):
            print("Email address is valid!")
            break
        else:
            print("Invalid Email - try again")
            continue
main()
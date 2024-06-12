import re

def valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def main():
    while True:
        email = input("Enter your email")

        if not emial.strip():
            print("Invalid Email")
            continue
main()
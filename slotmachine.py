MAX_LINES = 3 # constant vlue i.e. not going to change


def deposit():
    while True:
        amount = input("How much to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():




def main():
    balance = deposit()

main()
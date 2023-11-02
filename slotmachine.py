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
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")

    return lines



def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main()

def calculate_months_to_payoff(mortgage_value, interest_rate, term_years):
    monthly_interest_rate = interest_rate / 100 / 12
    term_months = term_years * 12
    monthly_payment = (mortgage_value * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -term_months)
    months_to_payoff = term_months
    return months_to_payoff

def main():
    mortgage_value = float(input("Enter remaining value of your mortgage: $"))
    interest_rate = float(input("Enter your interest rate as a percentage: "))
    term_years = int(input("Enter the term of your mortgage (years): "))
    months_to_payoff = calculate_months_to_payoff(mortgage_value, interest_rate, term_years)
    print("It will take approximately {} months to payoff your mortgage.".format(months_to_payoff))

if __name__ == "__main__":
    main()
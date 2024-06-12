def main():

    def calculate_months_to_pay_off(mortgage_value, interest_rate, term_years):
        monthly_interest_rate = interest_rate / 100 / 12
        term_months = term_years * 12
        monthly_payment = (mortgage_value * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -term_months)
        months_to_payoff = term_months
        return months_to_payoff

    mortgage_value = input("Enter remaining value of your mortgage: $")
    interest_rate = input("Enter your interest rate as a percentage: ")
    term_years = input("Enter the term of your mortgage: ")
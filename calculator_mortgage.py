def calculate_months(mortgage_value, interest, term):
    monthly_interest_rate = interest / 100 / 12
    term_months = term * 12
    monthly_payment = (mortgage_value * monthly_interest_rate) / (1 - (1 + monthly_interest) ** -term_months)
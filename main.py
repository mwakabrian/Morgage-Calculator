# Morgage Calculator

# Using the Loan Amortization formula below,

# M = P[i(1+i)^n]/(1+i)^n - 1]

# Where:
# M = Total monthly payment -7452.81
# P = Total principal loan amount - $100,000
# i = % monthly interest rate -7.5% (0.075 as a decimal)
# n = number of payments (loan duration in months)-30 years, so 30 * 12 = 360 months

# Defining parameters in Calculating Monthly payments
def calculate_monthly_payment(principal, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 100 / 12
    total_months = years * 12
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**-total_months)
    return monthly_payment

def main():
    principal = float(input("Enter the loan principal: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in percentage): "))
    years = int(input("Enter the number of years: "))
    
    monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
    
    print(f"Result...\nFor a {years}-Year mortgage loan of ${principal:.2f} at an annual interest rate of {annual_interest_rate:.2f}% you pay ${monthly_payment:.2f} Monthly")
    print(f"Total amount paid will be ${monthly_payment * years * 12:.2f}")

if __name__ == "__main__":
    main()
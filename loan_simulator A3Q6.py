def simulate_loan(loan_amount, annual_rate, monthly_payment):
    balance = loan_amount
    monthly_rate = annual_rate / 12 / 100
    months = 0

    # Prevent infinite loop if payment is too small
    if monthly_payment <= balance * monthly_rate:
        return None

    while balance > 0:
        balance += balance * monthly_rate
        balance -= monthly_payment
        months += 1

        if balance < 0:
            balance = 0

    return months


def main():
    loan_amount = float(input("Enter loan amount: "))
    annual_rate = float(input("Enter annual interest rate (in %): "))
    monthly_payment = float(input("Enter monthly payment: "))

    months = simulate_loan(loan_amount, annual_rate, monthly_payment)

    if months is None:
        print("Monthly payment is too low to pay off the loan.")
    else:
        print("\nLoan paid off!")
        print(f"It took {months} months to repay the loan.")


if __name__ == "__main__":
    main()

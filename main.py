import math
import sys


def calculate_emi(p, r, n):
    return (p * r * pow(1 + r, n)) / (pow(1 + r, n) - 1)


def cancel_simulation(amount):
    print("\nSimulation canceled.")
    print(f"No changes made to your profile. Projected savings of {round(amount, 2)} were not processed.\n")


def payment_gateway(total_saved):
    print("\nSelect simulation processing method (For Report Generation):")
    print("1. Net Banking")
    print("2. Debit Card")
    print("3. Credit Card")
    print("4. Phone Pe")
    print("5. Google Pay")
    print("6. Cancel")

    try:
        k = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Canceling.")
        cancel_simulation(total_saved)
        return

    if k == 6:
        cancel_simulation(total_saved)
    else:
        print("\nYour Simulation is Successful!")
        print("--- Final Booking Details ---")
        print("Status: Active Debt Reduction Plan")
        print("Bank: Simulated Processing")
        print(f"Projected Savings: {round(total_saved, 2)}")

        confirm = int(input("\nDo you want to save this profile? (1. Confirm, 2. Cancel): "))
        if confirm == 2:
            cancel_simulation(total_saved)
        else:
            print("\nThank you for using EMI Master! Your financial profile is saved.\n")


def simulate_loan():
    print("\n--- EMI Master & Prepayment Simulator ---")

    try:
        principal = float(input("Enter Loan Principal: "))
        annual_rate = float(input("Enter Annual Interest Rate (%): "))
        tenure_years = int(input("Enter Tenure in Years: "))
        prepayment = float(input("Enter Monthly Prepayment Amount (0 if none): "))
    except ValueError:
        print("Error: Please enter numeric values.")
        return

    monthly_rate = annual_rate / 1200
    total_months = tenure_years * 12

    standard_emi = calculate_emi(principal, monthly_rate, total_months)
    original_total_pay = standard_emi * total_months

    print(f"\nStandard EMI: {round(standard_emi, 2)}")
    print(f"Total Interest (No Prepayment): {round(original_total_pay - principal, 2)}")

    balance = principal
    month_count = 0
    total_interest_paid = 0

    while balance > 0:
        month_count += 1
        interest = balance * monthly_rate

        if (standard_emi + prepayment) > (balance + interest):
            total_interest_paid += interest
            balance = 0
        else:
            principal_paid = (standard_emi - interest) + prepayment
            total_interest_paid += interest
            balance -= principal_paid

        if month_count > (total_months * 2):
            break

    new_tenure_years = month_count / 12
    interest_saved = (original_total_pay - principal) - total_interest_paid

    print("-" * 40)
    print(f"New Tenure: {round(new_tenure_years, 2)} years")
    print(f"Months Saved: {total_months - month_count}")
    print(f"Interest Saved: {round(interest_saved, 2)}")
    print("-" * 40)

    payment_gateway(interest_saved)


def main():
    while True:
        print("1. EMI Master - Loan Simulator")
        print("2. Exit")

        choice = input("Select one of the options: ")

        if choice == '1':
            simulate_loan()
        elif choice == '2':
            print("Exiting System. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()

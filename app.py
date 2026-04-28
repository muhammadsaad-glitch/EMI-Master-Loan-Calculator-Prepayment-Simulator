import math

def calculate_emi(p, r, n):
    # Standard Amortization Formula
    emi = (p * r * pow(1 + r, n)) / (pow(1 + r, n) - 1)
    return emi

def simulate_loan():
    print("--- EMI Master & Prepayment Simulator ---")
    
    # Input Phase
    principal = float(input("Enter Loan Principal: "))
    annual_rate = float(input("Enter Annual Interest Rate (%): "))
    tenure_years = int(input("Enter Tenure in Years: "))
    prepayment = float(input("Enter Monthly Prepayment Amount (0 if none): "))

    # Formatting variables
    monthly_rate = annual_rate / (12 * 100)
    total_months = tenure_years * 12
    
    # Calculate Original Stats
    standard_emi = calculate_emi(principal, monthly_rate, total_months)
    original_total_pay = standard_emi * total_months
    
    print(f"\nStandard Monthly EMI: {round(standard_emi, 2)}")
    print(f"Total Interest without Prepayment: {round(original_total_pay - principal, 2)}")
    print("-" * 40)

    # Simulation Phase (The "Master" Logic)
    balance = principal
    month_count = 0
    total_interest_paid = 0

    while balance > 0:
        month_count += 1
        interest_for_month = balance * monthly_rate
        principal_paid = (standard_emi - interest_for_month) + prepayment
        
        total_interest_paid += interest_for_month
        balance -= principal_paid
        
        if month_count > total_months * 2: # Safety break
            break

    # Results Phase
    new_tenure_years = month_count / 12
    interest_saved = (original_total_pay - principal) - total_interest_paid

    print(f"New Tenure with Prepayments: {round(new_tenure_years, 2)} years")
    print(f"Months Saved: {total_months - month_count}")
    print(f"TOTAL INTEREST SAVED: {round(interest_saved, 2)}")
    print("-" * 40)

if __name__ == "__main__":
    simulate_loan()

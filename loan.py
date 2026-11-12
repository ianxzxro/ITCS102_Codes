loan_amt = float(input("Enter the loan amount: "))
years = int(input("Enter the number of years: "))
month = years * 12
principal = loan_amt / month
remaining_balance = loan_amt

print("|Month\t|\tMonthly Payment\t|\tInterest\t|\tPrincipal\t|\tRemaining Balance\t|")
for x in range(1, month + 1):
    remaining_balance -= principal
    loan_interest = remaining_balance * 0.00256
    monthly_payment = principal + loan_interest
    print(f"|{x}\t|\t{round(monthly_payment, 2)}\t\t|{round(loan_interest, 2)}\t\t\t|{round(principal, 2)}\t\t\t|{round(remaining_balance, 2)}\t\t\t\t|")



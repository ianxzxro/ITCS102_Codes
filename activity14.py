# age(integer)
# is_employed(boolean)
# credit_score(float)
# annual_income(float)
# has_collateral(boolean)

age = int(input("Enter your age ---> "))
is_employed = bool(input("Are you employed? (True/False) ---> "))
credit_score = float(input("Enter your credit score ---> "))
annual_income = float(input("Enter your annual income ---> "))
has_collateral = bool(input("Do you have collateral? (True/False) ---> "))

base_rate = 0.00

if age >= 21 and is_employed == True:
    print("Accepted Baseline Eligibility")
    if credit_score >= 750: #tier1
        print("You have a High Credit Score.")
        if annual_income >= 100000:
            print("You have a High Annual Income.")
            base_rate = 4.5
            print("Your base rate is:", base_rate)
        else:
            base_rate = 5.0 
            print("Your base rate is:", base_rate)
    elif credit_score >= 600 and credit_score < 750: #tier2
        print("You're credit score is less than 750")
        if has_collateral == True:
            print("You have collateral.")
            base_rate = 7.0
            print("Your base rate is:", base_rate)
        elif annual_income <= 40000:
            print("You have a Low Annual Income.")
            base_rate = 9.0
            print("Your base rate is:", base_rate)
        else:
            base_rate = 8.0
            print("Your base rate is:", base_rate)
    elif credit_score < 600: #tier3 
        print("Rejected: Credit score is too low.")
    else:
        print("Invalid details")

else:  
    print("You are not eligible.")



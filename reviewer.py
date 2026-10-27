#inputs
age = int(input("AGE --> "))
rev = float(input("REVENUE --> "))
cs = int(input("CREDIT SCORE --> "))
years_in_business = int(input("YEARS IN BUSINESS --> "))
has_defaults = bool(input("HAS DEFAULTS --> "))
collateral_name = input("COLLATERAL NAME --> ")
collateral_value = float(input("COLLATERAL VALUE --> "))

max_loan = 0
base_fee = 0

if age >= 21 and years_in_business >= 2.0 and has_defaults == False:
    print("APPROVED")
    if cs >= 720: #tier1
        print("CREDIT SCORE IS HIGH")
        max_loan = rev * 3
        print("MAX LOAN AMOUNT --> ", max_loan)
        if rev >= 50000:#revenue
            print("ABOVE 50K REVENUE")
            base_fee = max_loan * 0.015
            print("BASE FEE --> ", base_fee)
        else:
            base_fee = max_loan * 0.025
            print("BASE FEE --> ", base_fee)
        if collateral_value >= max_loan: #collateral
            print("COLLATERAL ",collateral_name,"with a value of",collateral_value," is ACCEPTED")
        else:
            print("Rejected : Insufficient collateral value for",collateral_value)
        if collateral_value % 5000 != 0: #subcharge
            base_fee += 250
            print("ADDITIONAL CHARGE HAS BEEN ADDED TO BASE FEE, total base fee is",base_fee)
        else:
            print("collateral value divisible by 5000")
    elif cs <= 620 and cs < 720 : #tier2
        print("CREDIT SCORE IS GOOD")
        max_loan = rev * 1.5
        print("MAX LOAN AMOUNT --> ",max_loan)
        if years_in_business >= 5.0: #yearsinbusiness
            base_fee = max_loan * 0.02
            print("YEARS IN BUSINESS GREATER THAN 5 YEARS BASEE FEE -->",base_fee)
        else:
            base_fee = max_loan * 0.035
            print("YEARS IN BUSINESS GREATER THAN 5 YEARS BASEE FEE -->",base_fee)
        if collateral_value >= max_loan: #collateral
            print("COLLATERAL ",collateral_name,"with a value of",collateral_value," is ACCEPTED")
        else:
            print("Rejected : Insufficient collateral value for",collateral_value)
        if collateral_value % 5000 != 0: #subcharge
            base_fee += 250
            print("ADDITIONAL CHARGE HAS BEEN ADDED TO BASE FEE, total base fee is",base_fee)
        else:
            print("collateral value divisible by 5000")
    elif cs> 620: #tier3
        print("Credit SCORE TOO LOW")
    else:
        print("INVALID DUE TO LOW CREDIT SCORE")
else:
    print("DENIED")


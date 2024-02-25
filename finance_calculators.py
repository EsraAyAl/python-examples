# this programs allows the user to access two diferent financial calculators:an investment calculator and a home loan repayment calculator


import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print("")
calculation=input("Enter either 'investment' or 'bond' from the menu above to proceed:")

print(calculation.lower())

if calculation.lower() != "investment" and calculation.lower() !="bond":
    print("You can enter investment or bond")
elif calculation.lower()== "investment":
    amount_of_money= int(input("How much money are they depositing?:"))
    interest_rate= float(input("The interest rate: "))
    investment_years= float(input("How many years do they plan on investing?:"))
    interest=str(input("Which interest do you want? (simple) or (compound):"))
    print(" the appropriate amount that they will get back after the given period, at the specified interest rate.")
    if interest=="simple":
        total_amount= amount_of_money* (1+ (interest_rate)/100 * investment_years)
        print(total_amount)
    else:
        total_amount= amount_of_money* math.pow(1+ (interest_rate)/100,investment_years)
        print(total_amount)   

else:
    present_value= int(input("Enter the present value of the house:"))
    interest_rate= float(input("Enter the interest rate:"))
    number_of_months= int(input("How many months do they plan to take to repay the bond?:"))

    repayment= (((interest_rate/100)/12)* present_value)/(1- (1+ ((interest_rate/100)/12))**(-number_of_months))
    print(repayment)


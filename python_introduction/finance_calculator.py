#assigning a variable
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

#calculate the monthly_savings and Projected_Savings
monthly_savings = float(monthly_income) - float(monthly_expenses)
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#print the result
print("Your monthly savings are $", monthly_savings)
print("Projected savings after one year, with interest, is: $", Projected_Savings)
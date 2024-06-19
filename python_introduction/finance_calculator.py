#assigning a variable
income = int(input("Enter your monthly income: "))
expense = int(input("Enter your total monthly expenses: "))

#calculate the monthly_savings and Projected_Savings
monthly_savings =  income - expense 
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#print the result
print("Your monthly savings are $", monthly_savings)
print("Projected savings after one year, with interest, is: $", Projected_Savings)
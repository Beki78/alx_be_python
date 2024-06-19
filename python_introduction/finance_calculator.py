#assigning a variable
income = int(input("Enter your monthly income: "))
expense = int(input("Enter your total monthly expenses: "))

#calculate the Monthly_Savings and Projected_Savings
Monthly_Savings =  income - expense 
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)

#print the result
print("Your monthly savings are $", Monthly_Savings)
print("Projected savings after one year, with interest, is: $", Projected_Savings)
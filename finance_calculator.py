# This script calculates the monthly savings based on user input for income and expenses.
monthly_expenses = float(input("Enter your monthly expenses: "))
total_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_expenses - total_expenses

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are: ${monthly_savings}")
print(f"Projected savings after one year with interest is: ${projected_savings}")
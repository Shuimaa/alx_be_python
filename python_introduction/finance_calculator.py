# Prompt the user for their monthly income
income = float(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses
expenses = float(input("Enter your total monthly expenses: "))

# Calculate the monthly savings
monthly_savings = income - expenses

# Project annual savings with 5% interest
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display the results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings}.")

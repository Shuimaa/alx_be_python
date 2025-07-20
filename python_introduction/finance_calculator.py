# finance_calculator.py

# قراءة الدخل الشهري من المستخدم
monthly_income = float(input("Enter your monthly income: "))

# قراءة المصاريف الشهرية من المستخدم
monthly_expenses = float(input("Enter your total monthly expenses: "))

# حساب التوفير الشهري
monthly_savings = monthly_income - monthly_expenses

# حساب التوفير السنوي مع الفائدة
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest

# طباعة النتائج
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")

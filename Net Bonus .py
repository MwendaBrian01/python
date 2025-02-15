# Get user input
salary = float(input("Enter your total salary: "))
years_of_service = int(input("Enter your years of service: "))

# Determine bonus percentage
if years_of_service > 10:
    bonus_percentage = 0.10
elif 6 <= years_of_service <= 10:
    bonus_percentage = 0.08
else:  # Less than 6 years
    bonus_percentage = 0.05


bonus_amount = salary * bonus_percentage
total_salary = salary + bonus_amount  


print(f"Your net bonus is: {bonus_amount:.2f}")
print(f"Your net salary is: {total_salary:.2f}")  

from abc import ABC, abstractmethod

# Abstract Base Class
class Employee(ABC):
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_salary(self):
        pass  


class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, base_salary, hourly_rate, hours_worked):
        super().__init__(emp_id, name, base_salary)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, base_salary, monthly_salary):
        super().__init__(emp_id, name, base_salary)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

# Example Usage
hourly_emp = HourlyEmployee(101, "Alice", 0, 20, 160)  
salaried_emp = SalariedEmployee(102, "Bob", 0, 5000)   

print(f"Hourly Employee Salary: {hourly_emp.calculate_salary()}") 
print(f"Salaried Employee Salary: {salaried_emp.calculate_salary()}")

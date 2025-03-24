class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, initial_balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return amount  # Return the amount deposited
        else:
            return "Invalid deposit amount. Amount must be positive."

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:  # Check for sufficient balance
                self.balance -= amount
                return amount  # Return the amount withdrawn
            else:
                return "Insufficient balance."
        else:
            return "Invalid withdrawal amount. Amount must be positive."

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")

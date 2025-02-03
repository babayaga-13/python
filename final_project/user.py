import random


class User:
    def __init__(self, name, email, address, acc_type):
        self.name = name
        self.email = email
        self.address = address
        self.acc_type = acc_type
        self.balance = 0
        self.account_number = email + str(random.randint(0, 100))
        self.transaction_history = []
        self.total_loan = 0
        self.loan_count = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        from admin import Admin

        if Admin.check_total_balance() < 2 * Admin.check_total_loan():
            print("The bank is bankrupt! Withdrawals are not allowed.")
        elif amount > self.balance:
            print("Withdrawal amount exceeded")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")

    def check_balance(self):
        return self.balance

    def show_transaction_history(self):
        return self.transaction_history

    def take_loan(self, loan_amount):
        from admin import Admin

        if not Admin.loan_enabled:
            print("Loan feature is currently disabled.")
        elif self.loan_count < 2:
            self.balance += loan_amount
            self.total_loan += loan_amount
            self.transaction_history.append(f"Loan taken: {loan_amount}")
            self.loan_count += 1
        else:
            print("Loan limit exceeded")

    def transfer(self, receiver, amount):
        from admin import Admin

        if receiver.account_number not in Admin.users:
            print("Account does not exist")
        elif self.balance >= amount:
            self.balance -= amount
            receiver.balance += amount
            self.transaction_history.append(f"Transferred: {amount} to {receiver.name}")
        else:
            print("Insufficient balance")

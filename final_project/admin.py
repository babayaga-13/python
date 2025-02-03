from user import User


class Admin:
    users = {}
    admin_password = "admin123"
    loan_enabled = True

    @classmethod
    def create_account(cls, name, email, address, acc_type):
        new_account = User(name, email, address, acc_type)
        cls.users[new_account.account_number] = new_account
        return new_account.account_number

    @classmethod
    def delete_account(cls, acc_number):
        if acc_number in cls.users:
            del cls.users[acc_number]
        else:
            print("Account not found")

    @classmethod
    def list_accounts(cls):
        for acc_number, user in cls.users.items():
            print(
                f"Account Number: {acc_number}, Name: {user.name}, Account Type: {user.acc_type}"
            )
        if len(cls.users) == 0:
            print("NO Available User")

    @classmethod
    def check_total_balance(cls):
        return sum(user.balance for user in cls.users.values())

    @classmethod
    def check_total_loan(cls):
        return sum(user.total_loan for user in cls.users.values())

    @classmethod
    def toggle_loan_feature(cls):
        cls.loan_enabled = not cls.loan_enabled
        print(f"Loan feature {'enabled' if cls.loan_enabled else 'disabled'}")

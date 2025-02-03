from admin import Admin

print("Welcome to Phitron Bank")
print("1. Admin Log-in")
print("2. Exit to system")

n = int(input("Enter your choice: "))

if n == 1:
    while True:
        print("************* Admin ***********")
        password = input("Enter admin password: ")
        if password == Admin.admin_password:
            print("Admin Login Successful!")
            print("Total Bank Balance:", Admin.check_total_balance())
            print("Total Loan Amount:", Admin.check_total_loan())

            while True:
                print("\nWelcome to the Bank Management System")
                print("1. Create Account\t2. Delete Account\t3. Deposit")
                print("4. Withdraw\t\t5. Check Balance\t6. Transaction History")
                print("7. Take Loan\t\t8. Transfer Money\t9. Total Balance")
                print("10. Total Loan\t\t11. Loan Toggle \t12. Current Users")
                print("13. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    name = input("Enter name: ")
                    email = input("Enter email: ")
                    address = input("Enter address: ")
                    acc_type = input("Enter account type (Savings/Current): ")
                    acc_number = Admin.create_account(name, email, address, acc_type)
                    print(
                        f"Account created successfully! Your account number is {acc_number}"
                    )

                elif choice == "2":
                    acc_number = input("Enter account number to delete: ")
                    Admin.delete_account(acc_number)

                elif choice == "3":
                    acc_number = input("Enter account number: ")
                    if acc_number in Admin.users:
                        amount = float(input("Enter amount to deposit: "))
                        Admin.users[acc_number].deposit(amount)
                        print("Amount deposited successfully.")
                    else:
                        print("Account not found.")

                elif choice == "4":
                    acc_number = input("Enter account number: ")
                    if acc_number in Admin.users:
                        amount = float(input("Enter amount to withdraw: "))
                        Admin.users[acc_number].withdraw(amount)
                        print("Amount withdrawn successfully.")
                    else:
                        print("Account not found.")

                elif choice == "5":
                    acc_number = input("Enter account number: ")
                    if acc_number in Admin.users:
                        print(f"Balance: {Admin.users[acc_number].check_balance()}")
                    else:
                        print("Account not found.")

                elif choice == "6":
                    acc_number = input("Enter account number: ")
                    if acc_number in Admin.users:
                        print(
                            "Transaction History:",
                            Admin.users[acc_number].show_transaction_history(),
                        )
                    else:
                        print("Account not found.")

                elif choice == "7":
                    acc_number = input("Enter account number: ")
                    if acc_number in Admin.users:
                        amount = float(input("Enter loan amount: "))
                        Admin.users[acc_number].take_loan(amount)
                        print("Loan granted.")
                    else:
                        print("Account not found.")

                elif choice == "8":
                    sender = input("Enter your account number: ")
                    receiver = input("Enter recipient's account number: ")
                    amount = float(input("Enter amount to transfer: "))

                    if sender in Admin.users and receiver in Admin.users:
                        Admin.users[sender].transfer(Admin.users[receiver], amount)
                        print("Amount transferred successfully.")
                    else:
                        print("One or both accounts not found.")

                elif choice == "9":
                    print("Total Balance:", Admin.check_total_balance())

                elif choice == "10":
                    print("Total Loan:", Admin.check_total_loan())

                elif choice == "11":
                    Admin.toggle_loan_feature()

                elif choice == "12":
                    Admin.list_accounts()

                elif choice == "13":
                    print("Exiting... Thank you!")
                    break

                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Incorrect password!")

elif n == 2:
    print("Exiting the system. Goodbye!")

else:
    print("Invalid input! Please enter a valid choice.")

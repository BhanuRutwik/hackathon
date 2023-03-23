#!/usr/bin/env python
# coding: utf-8

# In[2]:


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. New balance is {self.balance}.")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Current balance is {self.balance}.")

# Main program
accounts = {}

while True:
    print("\nSelect an option:")
    print("1. Create an account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter account name: ")
        balance = float(input("Enter initial balance (optional): "))
        accounts[name] = BankAccount(name, balance)
        print(f"Account for {name} created successfully.")

    elif choice == '2':
        name = input("Enter account name: ")
        if name in accounts:
            amount = float(input("Enter amount to deposit: "))
            accounts[name].deposit(amount)
        else:
            print(f"No account found for {name}.")

    elif choice == '3':
        name = input("Enter account name: ")
        if name in accounts:
            amount = float(input("Enter amount to withdraw: "))
            accounts[name].withdraw(amount)
        else:
            print(f"No account found for {name}.")

    elif choice == '4':
        name = input("Enter account name: ")
        if name in accounts:
            accounts[name].check_balance()
        else:
            print(f"No account found for {name}.")

    elif choice == '5':
        print("Thank you for using our banking system. Goodbye!")
        break

    else:
        print("Invalid choice. Please select an option between 1-5.")


# In[ ]:





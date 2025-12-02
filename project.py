class BankAccount:
    # Constructor
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.__balance = balance   # Encapsulation (private variable)

    # Method to deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    # Getter method to check balance
    def get_balance(self):
        return self.__balance

    # Method to show details
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self.__balance}")


# ------------------------------------
# Inheritance Example
# ------------------------------------

class SavingsAccount(BankAccount):
    def __init__(self, name, account_number, balance=0, interest_rate=5):
        super().__init__(name, account_number, balance)
        self.interest_rate = interest_rate

    # Polymorphism example
    def show_details(self):
        super().show_details()
        print(f"Interest Rate: {self.interest_rate}%")


# ------------------------------------
# Creating Objects and Using Methods
# ------------------------------------

acc1 = SavingsAccount("Rama Krishna", "12345", 1000)

acc1.show_details()

print("\n--- Transactions ---")

acc1.deposit(500)
acc1.withdraw(300)

print("\nFinal Balance:", acc1.get_balance())
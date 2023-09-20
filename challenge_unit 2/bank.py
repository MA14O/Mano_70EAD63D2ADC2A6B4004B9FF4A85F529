class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited Rs{amount}. New balance: Rs{self.__account_balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew Rs{amount}. New balance: Rs{self.__account_balance}"
        elif amount > self.__account_balance:
            return "Insufficient funds."
        else:
            return "Invalid withdrawal amount."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name}: Rs{self.__account_balance}"

# Testing the BankAccount class
if __name__ == "__main__":
    account = BankAccount("123456789", "deepan", 1000)

    print(account.display_balance())  # Display initial balance
    print(account.deposit(500))        # Deposit Rs500
    print(account.withdraw(200))       # Withdraw Rs200
    print(account.display_balance())  # Display updated balance
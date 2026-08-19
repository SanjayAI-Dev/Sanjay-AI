# 16_Encapsulation
# binding the data together
# self.name==>public
# self._name==>protected
# self.__name==>private

class BankAccount:

    def __init__(self, owner, balance):
        # Public attribute
        # It can be accessed directly from outside the class
        self.owner = owner

        # Private attribute
        # __balance cannot be accessed directly in the normal way
        self.__balance = balance

    def deposit(self, amount):
        # Deposit money into the account
        if amount > 0:
            # Update the private balance
            self.__balance += amount
            print(f"${amount} deposited")

    def withdraw(self, amount):
        # Withdraw money only if sufficient balance is available
        if amount <= self.__balance:
            # Update the private balance
            self.__balance -= amount
            print(f"${amount} withdrawn")
        else:
            # Display message if balance is insufficient
            print("Insufficient balance")

    def get_balance(self):
        # Return the private balance
        # This provides controlled access to __balance
        return self.__balance


# Create a BankAccount object
account = BankAccount("Jaya", 1000)

# Deposit $500 into the account
account.deposit(500)

# Withdraw $200 from the account
account.withdraw(200)

# Get and print the current balance
print(account.get_balance())


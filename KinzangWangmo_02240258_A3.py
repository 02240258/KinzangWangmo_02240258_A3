"""
CSF101 Assignment 3 - Banking Application (Console Version)
Author: Kinzang Wangmo
Student Number: 02240258
"""

# === Custom Exceptions ===
class InvalidInputError(Exception):
    """Raised when the user input is invalid."""
    pass

class InvalidTransferError(Exception):
    """Raised when a transfer attempt is invalid."""
    pass

# === BankAccount Class ===
class BankAccount:
    """A class representing a bank account."""

    def __init__(self, name, balance=0.0):
        """Initialize with name and optional balance."""
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Deposit funds into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Withdraw funds from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance < amount:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance

    def transfer(self, other_account, amount):
        """Transfer funds to another BankAccount."""
        if not isinstance(other_account, BankAccount):
            raise InvalidTransferError("Recipient must be a BankAccount.")
        self.withdraw(amount)
        other_account.deposit(amount)
        return self.balance

    def get_balance(self):
        """Return the account balance."""
        return self.balance

# === Top-Up Function ===
def topUpMobile(phone_number, amount):
    """
    Top up a mobile phone balance.
    """
    if len(phone_number) < 8 or not phone_number.isdigit():
        raise InvalidInputError("Invalid phone number.")
    if amount <= 0:
        raise ValueError("Top-up amount must be positive.")
    return f"Topped up Nu{amount:.2f} to {phone_number}."

# === Process User Input ===
def processUserInput(choice, account, other_account=None):
    """
    Process user menu input and perform the appropriate banking action.
    """
    try:
        if choice == "1":
            amt = float(input("Enter amount to deposit (Nu): "))
            account.deposit(amt)
            print(" Deposit successful.")

        elif choice == "2":
            amt = float(input("Enter amount to withdraw (Nu): "))
            account.withdraw(amt)
            print(" Withdrawal successful.")

        elif choice == "3":
            if other_account is None:
                raise InvalidTransferError("No recipient account specified.")
            amt = float(input("Enter amount to transfer (Nu): "))
            account.transfer(other_account, amt)
            print(f" Transferred Nu{amt:.2f} to {other_account.name}.")

        elif choice == "4":
            phone = input("Enter mobile phone number: ")
            amt = float(input("Enter top-up amount (Nu): "))
            message = topUpMobile(phone, amt)
            print("", message)

        elif choice == "5":
            print(f" Current Balance: Nu{account.get_balance():.2f}")

        elif choice == "0":
            print(" Exiting application...")

        else:
            raise InvalidInputError("Invalid menu choice.")

    except Exception as e:
        print(f" Error: {e}")

# === CLI Interface ===
def main():
    """
    Command-line interface for the banking app.
    """
    print("=== Welcome to the Banking Application ===")
    acc1 = BankAccount("Dupchu", 1000)  
    acc2 = BankAccount("Tshering", 500)     
    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Mobile Top-Up")
        print("5. Check Balance")
        print("0. Exit")
        choice = input("Select an option: ")
        if choice == "0":
            processUserInput(choice, acc1)
            break
        else:
            processUserInput(choice, acc1, acc2)

# === Entry Point ===
if __name__ == "__main__":
    main()
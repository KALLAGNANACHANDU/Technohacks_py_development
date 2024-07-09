class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

def main():
    atm = ATM(initial_balance=1000)  # Initialize ATM with a default balance
    while True:
        print("\nATM Menu")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ").strip()
        
        if choice == '1':
            print(f"Your current balance is: ${atm.check_balance():.2f}")
        
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            if atm.deposit(amount):
                print(f"Successfully deposited ${amount:.2f}.")
            else:
                print("Invalid amount. Please enter a positive number.")
        
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            if atm.withdraw(amount):
                print(f"Successfully withdrew ${amount:.2f}.")
            else:
                print("Invalid amount or insufficient funds.")
        
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

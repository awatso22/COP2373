class BankAcct:
    def __init__(self, name, acct_num, amount=0.0, interest_rate=0.01):
        self.name = name
        self.acct_num = acct_num
        self.amount = float(amount)
        self.interest_rate = float(interest_rate)

    def adjust_interest_rate(self, new_rate):
        """Adjust the interest rate (as a decimal)."""
        self.interest_rate = float(new_rate)

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.amount += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        """Withdraw money if funds are available."""
        if amount <= 0:
            print("Withdraw amount must be positive")
        elif amount > self.amount:
            print("Insufficient funds.")
        else:
            self.amount -= amount

    def get_balance(self):
        """Return the balance of the account."""
        return self.amount

    def calculate_interest(self, days):
        """Calculate interest earned over a number of days."""
        daily_rate = self.interest_rate / 365
        interest = self.amount * daily_rate * days
        return interest

    def __str__(self):
        """Return a formatted string showing account info."""
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.acct_num}\n"
                f"Balance: ${self.amount:,.2f}\n"
                f"Interest Rate: {self.interest_rate * 100:.2f}%")

def test_bank_acct():
    print("Creating account...")
    acct = BankAcct("Lana Rowe", "956478", 1000.00, 0.05)

    print("\nInitial account state:")
    print(acct)

    print("\nDepositing $600...")
    acct.deposit(600)
    print(acct)

    print("\nWithdrawing $300...")
    acct.deposit(300)
    print(acct)

    print("\nAdjusting interest rate to 5%...")
    acct.adjust_interest_rate(0.05)
    print(acct)

    print("\nCalculating 30 days of interest...")
    interest = acct.calculate_interest(30)
    print(f"Interest for 30 days: ${interest:,.2f}")

    print("\nFinal account state:")
    print(acct)

# Run the test function when the file is executed
if __name__ == "__main__":
    test_bank_acct()

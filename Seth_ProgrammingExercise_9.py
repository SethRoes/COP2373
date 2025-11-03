# Program that states the name, account number, amount and interest rate.

class BankAcct:
    def __init__(self, name, account_number, initial_balance=0, interest_rate=0.0):
        self.name = name
        self.account_number = account_number
        self.balance = initial_balance
        self.interest_rate = interest_rate
        self.interest_earned_on_interest = 0

    def update_interest_rate(self, new_rate):
        if new_rate >= 0:
            self.interest_rate = new_rate
        else:
            print("Interest rate cannot be negative.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_balance(self):
        return self.balance

    def calculate_interest(self, num_days):
        if num_days < 0:
            print("Number of days cannot be negative.")
            return
        daily_rate = self.interest_rate / 365
        interest_for_day = self.balance * daily_rate
        interest_for_period = interest_for_day * num_days
        self.balance += interest_for_period
        self.interest_earned_on_interest += interest_for_period
        print(f"Interest of ${interest_for_period:.2f} calculated for {num_days} days.")

    def __str__(self):
        return (
            f"Account Name: {self.name}\n"
            f"Account Number: {self.account_number}\n"
            f"Current Balance: ${self.balance:.2f}\n"
            f"Annual Interest Rate: {self.interest_rate:.2%}\n"
            f"Total Interest Earned: ${self.interest_earned_on_interest:.2f}"
        )


def test_bank_account():
    print("--- Initializing Account ---")
    account1 = BankAcct("John Doe", "123456789", 1000, 0.05)
    print(account1)
    print("-" * 25)

    print("--- Testing Deposits ---")
    account1.deposit(500)
    account1.deposit(200.50)
    account1.deposit(-100)  # Test invalid deposit
    print("-" * 25)

    print("--- Testing Withdrawals ---")
    account1.withdraw(300)
    account1.withdraw(2000)  # Test insufficient funds
    account1.withdraw(100)
    account1.withdraw(-50)  # Test invalid withdrawal
    print("-" * 25)

    print("--- Testing Interest ---")
    account1.update_interest_rate(0.06)
    print(f"Updated interest rate to: {account1.interest_rate:.2%}")
    account1.calculate_interest(30)  # Calculate interest for 30 days
    print("-" * 25)

    print("--- Testing Interest with 0 days ---")
    account1.calculate_interest(0)  # Test 0 days
    print("-" * 25)

    print("--- Final Account Status ---")
    print(account1)
    print("-" * 25)

    print("--- Testing Negative Interest Rate ---")
    account1.update_interest_rate(-0.01)  # Test negative interest rate
    print("-" * 25)


test_bank_account()

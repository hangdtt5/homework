from bank_account import BankAccount

class SavingAccount(BankAccount):
    monthly_interest_rate = 0.005
   
    def calculate_interest(self):
        return self.monthly_interest_rate*self.balance



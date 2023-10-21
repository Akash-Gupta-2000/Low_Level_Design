class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def calculate_balances(self, user):
        balances = {}
        for expense in self.expenses:
            # Implement balance calculation logic here
            pass
        return balances

    def show_balances(self, user):
        balances = self.calculate_balances(user)
        for u, amount in balances.items():
            if amount > 0:
                print(f"{user.user_id} owes {u.user_id}: {amount:.2f}")
            elif amount < 0:
                print(f"{u.user_id} owes {user.user_id}: {abs(amount):.2f}")

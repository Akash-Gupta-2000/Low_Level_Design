class Group:
    def __init__(self, group_id, name, users):
        self.group_id = group_id
        self.name = name
        self.users = users
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

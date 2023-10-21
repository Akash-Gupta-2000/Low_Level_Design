from enums import ExpenseType
from user import User
from expense import Expense
from group import Group
from expense_manager import ExpenseManager

if __name__ == "__main__":
    expense_manager = ExpenseManager()

    user1 = User(1, "User1", "user1@example.com", "123-456-7890")
    user2 = User(2, "User2", "user2@example.com", "987-654-3210")
    user3 = User(3, "User3", "user3@example.com", "555-555-5555")

    group1 = Group(1, "Group1", [user1, user2, user3])

    expense_manager.add_expense(Expense(1, user1, [user1, user2, user3], ExpenseType.EQUAL, [100.0]))

    expense_manager.add_expense(Expense(2, user2, [user2, user3], ExpenseType.EXACT, [25.0, 75.0]))

    expense_manager.show_balances(user1)

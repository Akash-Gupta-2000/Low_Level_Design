from user import User


class SocialNetwork:
    def __init__(self):
        self.users = []

    def create_user(self, name, email, password):
        user_id = len(self.users) + 1
        user = User(user_id, name, email, password)
        self.users.append(user)
        return user

    def send_notification(self, user, content):
        # Implement notification sending logic
        pass

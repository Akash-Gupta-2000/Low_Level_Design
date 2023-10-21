class User:
    def __init__(self, username, is_member=False):
        self.username = username
        self.is_member = is_member
        self.badges = []  # List of earned badges
        self.questions = []
        self.answers = []

    def post_question(self, question):
        self.questions.append(question)

    def post_answer(self, answer):
        self.answers.append(answer)

    def add_comment(self, post, comment):
        post.add_comment(comment)

    def upvote(self, post):
        post.upvotes += 1

    def add_bounty(self, question, bounty_amount):
        question.add_bounty(bounty_amount)

    def add_badge(self, badge):
        self.badges.append(badge)

    def flag_post(self, post, reason):
        post.flag(reason)

    def close_question(self, question):
        question.close()

    def add_tag(self, question, tag):
        question.add_tag(tag)

    def vote_to_delete(self, question):
        question.vote_to_delete()

    def vote_to_close(self, question):
        question.vote_to_close()

class Moderator(User):
    def close_question(self, question):
        question.close()

    def undelete_question(self, question):
        question.undelete()

class Badge:
    def __init__(self, name, description):
        self.name = name
        self.description = description

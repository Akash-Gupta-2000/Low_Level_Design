class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.comments = []
        self.upvotes = 0
        self.flags = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def upvote(self):
        self.upvotes += 1

    def flag(self, reason):
        self.flags.append(reason)

class Question(Post):
    def __init__(self, author, content):
        super().__init__(author, content)
        self.bounty = 0
        self.tags = []
        self.answers = []
        self.closed = False
        self.deleted = False
        self.vote_to_close_count = 0
        self.vote_to_delete_count = 0

    def add_tag(self, tag):
        self.tags.append(tag)

    def add_bounty(self, bounty_amount):
        self.bounty += bounty_amount

    def vote_to_close(self):
        self.vote_to_close_count += 1

    def vote_to_delete(self):
        self.vote_to_delete_count += 1

    def close(self):
        self.closed = True

    def undelete(self):
        self.deleted = False
    
    def add_answer(self, answer):
        self.answers.append(answer)

class Answer(Post):
    def __init__(self, author, content):
        super().__init__(author, content)

class Comment:
    def __init__(self, author, text):
        self.author = author
        self.text = text

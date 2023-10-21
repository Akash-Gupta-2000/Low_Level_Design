class Post:
    def __init__(self, post_id, user, content):
        self.post_id = post_id
        self.user = user
        self.content = content
        self.comments = []
        self.likes = []
        self.shares = []

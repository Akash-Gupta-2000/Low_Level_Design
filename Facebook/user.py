class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.friends = []
        self.followers = []
        self.posts = []
        self.groups = []
        self.pages = []
        self.recommendations = []
        self.privacy_lists = []

    def send_friend_request(self, user):
        # Implement friend request logic
        pass

    def accept_friend_request(self, user):
        # Implement friend request acceptance logic
        pass

    def follow_user(self, user):
        # Implement follow user logic
        pass

    def create_group(self, name):
        # Implement group creation logic
        pass

    def join_group(self, group):
        # Implement group joining logic
        pass

    def create_page(self, name):
        # Implement page creation logic
        pass

    def follow_page(self, page):
        # Implement page following logic
        pass

    def create_post(self, content, privacy_list=None):
        # Implement post creation logic
        pass

    def add_comment(self, post, content):
        # Implement comment creation logic
        pass

    def like_post(self, post):
        # Implement post liking logic
        pass

    def share_post(self, post):
        # Implement post sharing logic
        pass

    def send_message(self, user, content):
        # Implement messaging logic
        pass

    def create_privacy_list(self, name, friends):
        # Implement privacy list creation logic
        pass

    def link_post_to_privacy_list(self, post, privacy_list):
        # Implement post privacy logic
        pass

    def add_recommendation(self, page, content):
        # Implement recommendation logic
        pass

    def search_posts(self, keyword):
        results = []
        for post in self.posts:
            if keyword in post.content:
                results.append(post)
        return results

    def search_groups(self, keyword):
        results = []
        for group in self.groups:
            if keyword in group.name:
                results.append(group)
        return results

from user import User
from group import Group
from page import Page
from post import Post
from comment import Comment
from notification import Notification
from privacy_list import PrivacyList
from social_network import SocialNetwork

# Create a social network
social_network = SocialNetwork()

# Create users
user1 = social_network.create_user("User1", "user1@example.com", "password1")
user2 = social_network.create_user("User2", "user2@example.com", "password2")

# User1 sends a friend request to User2
user1.send_friend_request(user2)

# User2 accepts the friend request
user2.accept_friend_request(user1)

# User1 follows User2
user1.follow_user(user2)

# User1 creates a group
group1 = user1.create_group("Group 1")

# User2 joins the group
user2.join_group(group1)

# User1 creates a page
page1 = user1.create_page("Page 1")

# User2 follows the page
user2.follow_page(page1)

# User1 creates posts
post1 = user1.create_post("Hello, World!")
post2 = user1.create_post("Hello, friends!")
post3 = user1.create_post("Good morning!")

# User2 adds a comment to a post
comment1 = user2.add_comment(post1, "Nice post!")

# User1 likes a post
user1.like_post(post1)

# User2 shares a post
user2.share_post(post1)

# User1 sends a message to User2
user1.send_message(user2, "Hi, how are you?")

# User1 creates a privacy list
privacy_list1 = user1.create_privacy_list("Close Friends", [user2])

# Link a post to the privacy list
user1.link_post_to_privacy_list(post1, privacy_list1)

# User1 adds a recommendation for the page
user1.add_recommendation(page1, "Great content!")

# Search for posts containing the keyword "Hello"
results = user1.search_posts("Hello")
for post in results:
    print(f"Found a post: {post.content}")

# Search for groups containing the keyword "Group"
results = user1.search_groups("Group")
for group in results:
    print(f"Found a group: {group.name}")

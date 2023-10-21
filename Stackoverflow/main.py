from user import User, Moderator, Badge
from post import Question, Answer, Comment
from system import System
from tag import Tag

def main():
    system = System()

    # Create users
    user1 = User("User1", is_member=True)
    user2 = User("User2", is_member=True)
    mod = Moderator("Moderator", is_member=True)

    # Create a badge
    helpful_badge = Badge("Helpful Badge", "Earned for being helpful")

    # Create and post questions
    question1 = Question(user1, "How to use Python dictionaries?")
    question2 = Question(user2, "Best practices for Python decorators?")
    system.questions.extend([question1, question2])

    # Add tags to questions
    python_tag = Tag("Python")
    system.tags.append(python_tag)
    question1.add_tag(python_tag)

    # Create and post answers
    answer1 = Answer(user2, "You can use Python dictionaries by...")
    answer2 = Answer(user1, "Python decorators are a powerful...")
    system.answers.extend([answer1, answer2])

    # Add answers to questions
    question1.add_answer(answer1)
    question2.add_answer(answer2)

    # Add comments
    comment1 = Comment(user1, "This is a great question!")
    comment2 = Comment(user2, "I found the answer very helpful.")
    question1.add_comment(comment1)
    answer1.add_comment(comment2)

    # Upvote posts
    user1.upvote(question1)
    user2.upvote(answer2)

    # Flag posts
    user1.flag_post(question2, "Inappropriate content")
    user2.flag_post(answer1, "Spam")

    # Add a bounty
    user1.add_bounty(question2, 50)

    # Assign a badge to a user
    user2.add_badge(helpful_badge)

    # Close a question
    mod.close_question(question1)

    # Print frequent tags
    frequent_tags = system.identify_frequent_tags(2)
    print("Frequently Used Tags:", frequent_tags)

if __name__ == "__main__":
    main()

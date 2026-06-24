from insta_utils.likes import like_count
from insta_utils.comments import comment_count

likes = int(input("Enter current likes: "))
comments = int(input("Enter current comments: "))

increment_likes = int(input("How many new likes? "))
new_comments = int(input("How many new comments? "))

likes = like_count(likes, increment_likes)
comments = comment_count(comments, new_comments)

print("\nAfter Update")
print("Likes:", likes)
print("Comments:", comments)
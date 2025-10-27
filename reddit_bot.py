import praw
import os

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent="script:PineappleBot:v1.0 (by u/PineappleUnited3368)"
)

print("Logged in as:", reddit.user.me())

subreddit = reddit.subreddit("testbot_naman")
subreddit.submit(
    title="Hello from my Reddit Bot!",
    selftext="This is my first automated post using PRAW. 🚀"
)
# fetch recent posts 
for submission in reddit.subreddit("python").hot(limit=5):
    print(f"title: {submission.title}")
    print(f"url: {submission.url}")
    print("----")

# auto reply if someone says "hello bot "
for comment in subreddit.stream.comments(skip_existing=True):
    if "hello bot" in comment.body.lower():
        comment.reply("Hey there! Bot here to say hi!")
        print("Replied to a comment")
        print("----")

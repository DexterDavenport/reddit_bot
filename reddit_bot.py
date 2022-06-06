import praw
import re
import time

reddit = praw.Reddit(client_id="mfru5Si-_N0QWajuWLlBDg", 
        client_secret="lzaH8k4jsUzRlHxrA5kWmJh9aET4uw",
        user_agent="<console:reddit_bot:0.0.1 (by /u/iam_ben)>",
        username="iam_ben",
        password="thisisben")

subreddits = ["antimeme", "Unexpected", "funny"]

pos = 0
title = ("I am Ben, but this is not a photo of me")
content = ("https://image.shutterstock.com/image-photo/stopno-kick-me-young-man-260nw-55156213.jpg")

def post():
    global subreddits
    global pos

    subreddit = reddit.subreddit(subreddits[pos])
    subreddit.submit(title, url = content)

    pos += 1

    if (pos <= len(subreddits) - 1):
        post()
    else:
        print("done")

post()
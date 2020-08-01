import getopt
import praw
import requests
import sys


def download(title, url, directory):
    reqst = requests.get(url)
    with open(directory + title, "wb") as file:
        file.write(reqst.content)


reddit = praw.Reddit(client_id="pO9TuXycwz04UQ",
                     client_secret="NaGQ8jNp8KhsNB9gwQAdaiXjX_c",
                     user_agent="top 10 wallpapers of the day")

argv = sys.argv[1:]
opts, args = getopt.getopt(argv, 'l:e:')

directory ='./'

for op in opts:
    if op[0] == '-l':
        directory = op[1]
    elif op[0] == '-e':
        print(op[1])

for submission in reddit.subreddit("wallpapers").top(limit=10):
    print(submission.title)
    print(submission.url)
    print("----------------------------------------------------------------------------")
    download(submission.title, submission.url, directory)

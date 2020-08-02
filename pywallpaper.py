import getopt
import praw
import requests
import sys
import os


def download(title, url, directory):
    reqst = requests.get(url)
    with open(directory + title + ".jpg", "wb") as file:
        file.write(reqst.content)


reddit = praw.Reddit(client_id="pO9TuXycwz04UQ",
                     client_secret="NaGQ8jNp8KhsNB9gwQAdaiXjX_c",
                     user_agent="top 10 wallpapers of the day")

argv = sys.argv[1:]
opts, args = getopt.getopt(argv, 'l:r:')

directory = './'
subredd = "wallpapers"

for op in opts:
    if op[0] == '-l':
        directory = op[1]
    elif op[0] == '-r':
        subredd = op[1]

for submission in reddit.subreddit(subredd).hot(limit=10):
    for width in range(os.get_terminal_size()[0]):
        print("-", end='')
    print(submission.title)
    print(submission.url)
    pic_title = submission.title.replace('/', '_')
    download(pic_title.replace(' ', '_'), submission.url, directory)

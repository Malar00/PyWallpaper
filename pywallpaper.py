import getopt
import praw
import requests
import sys
import os


def download(title, url, directory):
    reqst = requests.get(url)
    with open(directory + title + ".jpg", "wb") as file:
        file.write(reqst.content)


wallpapers = []


def cli(directory):
    for filename in os.listdir(directory):
        if filename.endswith('jpg'):
            wallpapers.append(filename)
    for wall in wallpapers:
        print(str(wallpapers.index(wall)) + ') ' + wall)
    choice = int(input("choose wallpaper from [0-" + str(len(wallpapers) - 1) + "]: "))
    os.system("feh --bg-scale " + directory + wallpapers[choice])
    os.system("wal -i " + directory + wallpapers[choice])


def replace_problematic(title):
    words = ['/', '(', ')', '\"', ' ', '[', ']', ',', '\'']
    for word in words:
        title = title.replace(word, '_')
    return title


reddit = praw.Reddit(client_id="pO9TuXycwz04UQ",
                     client_secret="NaGQ8jNp8KhsNB9gwQAdaiXjX_c",
                     user_agent="top 10 wallpapers of the day")

argv = sys.argv[1:]
opts, args = getopt.getopt(argv, 'l:r:i')

directory = './'
subredd = "wallpapers"

for op in opts:
    if op[0] == '-l':
        directory = op[1]
    if op[0] == '-r':
        subredd = op[1]
    if op[0] == '-i':
        cli(directory)
        exit()

for submission in reddit.subreddit(subredd).hot(limit=10):
    for width in range(os.get_terminal_size()[0]):
        print("-", end='')
    print(submission.title)
    print(submission.url)
    download(replace_problematic(submission.title), submission.url, directory)

import getopt
import sys
import praw
import requests
import os

wallpapers = []

argv = sys.argv[1:]
opts, args = getopt.getopt(argv, 'l:r:i')

directory_global = './'
subredd_global = "wallpapers"

reddit = praw.Reddit(client_id="pO9TuXycwz04UQ",
                     client_secret="NaGQ8jNp8KhsNB9gwQAdaiXjX_c",
                     user_agent="top 10 wallpapers of the day")


def download(title, url, directory_download):
    reqst = requests.get(url)
    with open(directory_download + title + ".jpg", "wb") as file:
        file.write(reqst.content)


def cli(directory_cli):
    for filename in os.listdir(directory_cli):
        if filename.endswith('jpg'):
            wallpapers.append(filename)
    for wall in wallpapers:
        print(str(wallpapers.index(wall)) + ') ' + wall)
    choice = int(input("choose wallpaper from [0-" + str(len(wallpapers) - 1) + "]: "))
    os.system("feh --bg-scale " + directory_cli + wallpapers[choice])
    os.system("wal -i " + directory_cli + wallpapers[choice])


def replace_problematic(title):
    words = ['/', '(', ')', '\"', ' ', '[', ']', ',', '\'']
    for word in words:
        title = title.replace(word, '_')
    return title


def APIget(directory_api, subredd_api):
    for submission in reddit.subreddit(subredd_api).hot(limit=10):
        for width in range(os.get_terminal_size()[0]):
            print("-", end='')
        print(submission.title)
        print(submission.url)
        download(replace_problematic(submission.title), submission.url, directory_api)


for op in opts:
    if op[0] == '-l':
        directory_global = op[1]
    if op[0] == '-r':
        subredd_global = op[1]
    if op[0] == '-i':
        cli(directory_global)
        exit()

APIget(directory_global, subredd_global)

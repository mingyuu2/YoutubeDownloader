import sys
import os
from pytube import YouTube

DOWNLOAD_FOLDER = './Youtube'

if len(sys.argv) == 1:
    print("Error: Insufficient arguments")
    sys.exit()

# set the urls array
urls = []
urls = sys.argv
del urls[0]


# Make directory when it is not exist
if not os.path.exists(DOWNLOAD_FOLDER):
    os.mkdir(DOWNLOAD_FOLDER)
else:
    pass


# take the info of youtube video
for url in urls:
    yt = YouTube(url)

    print("title : ", yt.title)
    print("length : ", yt.length)
    print("author : ", yt.author)
    print("publish date : ", yt.publish_date)
    print("views : ", yt.views)
    print("keywords : ", yt.keywords)
    print("description : ", yt.description)
    print("thumbnail url : ", yt.thumbnail_url)

    # download
    stream = yt.streams.get_highest_resolution()
    stream.download(DOWNLOAD_FOLDER)
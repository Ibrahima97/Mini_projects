from pytube import YouTube
from sys import argv

link= argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

#print("Info: ", yt.vid_info)

yd = yt.streams.get_highest_resolution()

# ADD FOLDER HERE
yd.download('./YTfolder')
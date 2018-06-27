from pytube import YouTube
import os
print("make sure it is english")


def download_v():
    yt = YouTube(video)
    print(str(yt.title))
    s = yt.streams.first()
    s.download()
    print("done")
while True:
    video = input("link:")
    dire = input(" directory for download:")
    os.chdir(dire)
    download_v()

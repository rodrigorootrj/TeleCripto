import requests
from pytube import YouTube, Channel
class Overmind:
    def main():
        yt = YouTube("https://youtu.be/T_Z7DwMROsQ")
        data = yt.vid_info['videoDetails']['viewCount']
        print(data)
Overmind.main()

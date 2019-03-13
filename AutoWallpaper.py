import re
import praw
import ctypes
import requests

import urllib.request

from bs4 import BeautifulSoup
from loguru import logger

def GetWallpaperURL():
    reddit = praw.Reddit(client_id='CLIENT ID',client_secret='CLIENT SECTRET',user_agent='USER AGENT')
    for submission in reddit.subreddit('ultrahdwallpapers').top('day',limit=1):
        WallpaperURL = submission.url + '1920x1080/'
    return WallpaperURL


def DownloadAndSetWallpaper(requestData,WallpaperFilePath):
    with open(WallpaperFilePath, 'wb') as f:  
        f.write(requestData.content)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, WallpaperFilePath , 0)

def ScrapeSite(requestData):
    soup = BeautifulSoup(requestData.text, "html.parser")
    for i in soup.find_all('meta'):
        if i.get('content'):
            if re.search(r'(https).*(jpg)', i.get('content')):
                MyLink = i.get('content')
    return MyLink

def main():
    wpURL = GetWallpaperURL()
    logger.info(f"Wallpaper URL is {wpURL}")
    r = requests.get(wpURL)
    logger.info(f"Scraping data...")
    MyLink = ScrapeSite(r)
    logger.info(f"Wallpaper download URL is {MyLink}")
    r = requests.get(MyLink)
    logger.info(f"Setting wallpaper...")
    DownloadAndSetWallpaper(r,FilePathToDownloadFolder')

if __name__ == "__main__":
    main()



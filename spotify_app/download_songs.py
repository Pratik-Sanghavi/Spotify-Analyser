from bs4 import BeautifulSoup
from requests.api import get
from requests_html import HTMLSession
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import os
import youtube_dl
import requests
import pandas as pd
from pathlib import Path

def get_id_from_title(song_title):
    prefix_url = "http://www.youtube.com/results?search_query="
    
    url = prefix_url+song_title
    url = url.replace(" ","+")
    options = Options()
    options.set_headless(headless=True)
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    soup  = BeautifulSoup(html, 'html.parser')
    result = soup.find('a', id="video-title")
    result = result['href'].split('/watch?v=')[1]
    return result

def download_mp3_songs(youtube_id,title):
    save_loc = "./Songs/"
    if not os.path.exists(save_loc):
        os.makedirs(save_loc)
    else:
        for f in os.listdir(save_loc):
            os.remove(os.path.join(save_loc, f))
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': save_loc + '/%(title)s.%(ext)s',
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(["https://www.youtube.com/watch?v="+youtube_id])
    except Exception as e:
        print(e)

def download_from_title(title):
    res = get_id_from_title(title)
    download_mp3_songs(res, title)
import requests
from bs4 import BeautifulSoup
import re
import os
import pathlib
import time

CURRENT_DIR = str(pathlib.Path(__file__).parent.resolve())
CORPUS_DIR = CURRENT_DIR + '/corpus'


def parse_lyrics_page(url):
    base_address = url.split('/lyrics/')[0]
    artist = url.split('/lyrics/')[1].split('/')[0]
    current_page = requests.get(url)
    soup = BeautifulSoup(current_page.content, "html.parser")
    title_tag = soup.find_all("b")[1]
    lyrics_tag = title_tag.find_next("div")

    title = title_tag.text
    lyrics = lyrics_tag.text
    # print(base_address)
    # print(title)
    # print(artist)

    if not os.path.exists(CORPUS_DIR):
        # Create a new directory because it does not exist
        os.makedirs(CORPUS_DIR)
        print("The new directory is created!")
    with open(f'{CORPUS_DIR}/{artist}.txt', 'a') as f:
        f.write(lyrics)


def get_lyrics_by_artist(artist, year_from=1960, year_to=1970):
    base_address = 'https://www.azlyrics.com'
    url = f'{base_address}/{artist[0]}/{artist}.html'
    current_page = requests.get(url)
    soup = BeautifulSoup(current_page.content, "html.parser")
    song_tags = soup.find_all("div", {"class": "listalbum-item"})
    for song in song_tags:
        print(song)
        time.sleep(3)
        release = song.find_previous("div", {"class": "album"})
        if release.text.split(":")[0] == "album" \
                and (int(release.text[-5:-1]) <= year_to) \
                and (int(release.text[-5:-1]) >= year_from):
            # print(release.text.split(":")[1][:-6])
            # print(song)
            if song.find("a", href=True):
                target_url = song.find("a", href=True)["href"]
                print(target_url)
                parse_lyrics_page(base_address + target_url)
        if release.text.split(":")[0] == "album" \
                and (int(release.text[-5:-1]) > year_to):
            return


get_lyrics_by_artist('zombies')

#parse_lyrics_page('https://www.azlyrics.com/lyrics/kinks/igottagonow.html')


# TODO:get song lyrics from song number N
        #song_album =


    #for release in album_tags:
        # print(release.text)
        #


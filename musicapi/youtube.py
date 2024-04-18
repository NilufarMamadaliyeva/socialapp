from pytube import YouTube
from youtube_search import YoutubeSearch
import os

def search_song(title, subtitle):
    query = f"{title} {subtitle}"
    search_results = YoutubeSearch(query, max_results=1).to_dict()
    return search_results

import os
import shutil

def download_song(youtube_url):
    try:
        yt = YouTube(youtube_url)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=os.path.join(os.path.expanduser("~"), "Downloads"))

        # Fayl nomini mp3-ga o'zgartiramiz
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"

        # Agar yangi fayl allaqachon mavjud bo'lsa, nomni ozgartiramiz
        count = 1
        while os.path.exists(new_file):
            new_file = f"{base}({count}).mp3"
            count += 1

        # Eski faylni o'chiramiz, agar fayl mavjud bo'lsa
        if os.path.exists(new_file):
            os.remove(new_file)

        # Yangi nom bilan faylni o'zgartiramiz
        os.rename(out_file, new_file)
        print(f"Downloaded: {new_file}")
        return True
    except Exception as e:
        print("Error:", e)
        return False



def search_and_download_song(title, subtitle):
    search_results = search_song(title, subtitle)
    for result in search_results:
        youtube_url = f"https://www.youtube.com/watch?v={result['id']}"
        if download_song(youtube_url):
            break

# Munisa Rizayeva & Konsta - O'ylamading
title = "O'ylamading"
subtitle = "Munisa Rizayeva & Konsta"
search_and_download_song(title, subtitle)

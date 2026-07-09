import requests
import re

SOURCE_URL = "http://azrogo.com/m3u8/artv/live/playlist.m3u8"
OUTPUT_FILE = "playlist.m3u"

def fetch_new_url():
    r = requests.get(SOURCE_URL, timeout=10)
    if r.status_code != 200:
        raise Exception("Failed to fetch playlist")

    content = r.text

    match = re.search(r'token=([A-Za-z0-9+/=]+)', content)
    if not match:
        raise Exception("Token not found")

    token = match.group(1)
    final_url = f"{SOURCE_URL}?token={token}"
    return final_url

def update_playlist(url):
    with open(OUTPUT_FILE, "w") as f:
        f.write("#EXTM3U\n")
        f.write("#EXTINF:-1, Auto Updated IPTV\n")
        f.write(url + "\n")

if __name__ == "__main__":
    new_url = fetch_new_url()
    update_playlist(new_url)
    print("Updated playlist with:", new_url)

with open("playlist.m3u", "w") as f:
    f.write("#EXTM3U\n")
    f.write("#EXTINF:-1, Updated by GitHub\n")
    f.write("http://example.com/test\n")

print("Playlist updated.")

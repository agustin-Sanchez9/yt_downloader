from pytube import Playlist

correct_playlist = False

while not correct_playlist:
    
    print("")
    link = input("Paste link here: ")
    p = Playlist(link)
    print("")

    print("Title: ", p.title)

    verification = input("Is this the video you like to download? (y/n) ")

    if verification == "y":
        correct_playlist = True
    elif verification == "n":
        pass
        
print("Wait for the download to finish")
for video in p.videos:
    video.streams.get_highest_resolution().download()
print("Playlist downloaded successfully")

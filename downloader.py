from pytube import YouTube


correct_video = False

while not correct_video:
    
    print("")
    link = input("Paste link here: ")
    yt = YouTube(link)
    print("")

    print("Title: ", yt.title)
    print("Views: ", yt.author)

    verification = input("Is this the video you like to download? (y/n) ")

    if verification == "y":
        correct_video = True
    elif verification == "n":
        pass
        
print("Wait for the download to finish")
yd = yt.streams.get_highest_resolution()
yd.download("C:/Users/Usuario/Desktop/mio/videos")
print("Video downloaded successfully")

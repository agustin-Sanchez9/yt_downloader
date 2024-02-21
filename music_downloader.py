from pytube import YouTube
import os

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
yd = yt.streams.get_audio_only()
out_file = yd.download("C:/Users/Usuario/Desktop/general/music")

base, ext = os.path.splitext(out_file) 
new_file = base + '.mp3'
os.rename(out_file, new_file) 

print("Video downloaded successfully")

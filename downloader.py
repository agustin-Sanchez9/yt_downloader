from pytube import YouTube

print("")
link = input("Paste link here: ")
yt = YouTube(link)
print("")
print("Title: ", yt.title)
print("Views: ", yt.views)
print("Wait for the download to finish")
yd = yt.streams.get_highest_resolution()
yd.download("C:/Users/Usuario/Desktop/mio/videos")
print("Video downloaded successfully")

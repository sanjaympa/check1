from pytube import YouTube
#link = "https://www.youtube.com/watch?v=xhPQhSqx7JA" #link for any videos
link = input("Please enter link which video you want to download : ")#"https://www.youtube.com/watch?v=xhPQhSqx7JA"
youtube_1=YouTube(link)
print(youtube_1.title)
print(youtube_1.thumbnail_url)
videos = youtube_1.streams.all()
#videos = youtube_1.streams.filter(Only_audio=True) #only Audio
vid = list(enumerate(videos))
for i in vid:
    print(i)
print ()
strm = int(input("enter: "))
videos[strm].download()
print("Successfully")
#******* Playlist******
#from pytube import Playlist
#py = Playlist("URL")
#print(f'Downloading:{py.title}')
#for video in py.videos:
 #   video.streams.first().download()






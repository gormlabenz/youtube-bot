from pytube import YouTube

yt = YouTube('https://youtube.com/watch?v=2lAe1cqCOXo', 2)
print(yt.streams)
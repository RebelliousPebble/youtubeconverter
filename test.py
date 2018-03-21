from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=8haPaV0YBPI')
vids = yt.streams.filter(only_video=True).filter(subtype='mp4').all()
for i in vids:
    print('Stream:')
    print(i)
    print('Resolution:')
    print(i.res)
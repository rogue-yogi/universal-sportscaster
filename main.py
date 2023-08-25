from pytube import YouTube

# Download YouTube video
video_url = 'your_youtube_video_url_here'
yt = YouTube(video_url)
video_stream = yt.streams.get_highest_resolution()
video_stream.download('/videos/.')



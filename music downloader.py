# yt-dlp python
# pip install yt-dlp
# pip install imageio-ffmpeg
import yt_dlp
video_url ="https://www.youtube.com/watch?v=AfWqNChGoxk"

# configuration options (mimics command-line flags)
ydl_opts = {
    'format':"bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192", #you can change to 320or 0
        }

    ]



}
#use a context manager to handle the download
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

    print("download complete!")



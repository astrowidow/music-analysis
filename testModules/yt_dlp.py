from yt_dlp import YoutubeDL

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [
        {'key': 'FFmpegExtractAudio',
         'preferredcodec': 'mp3',
         'preferredquality': '192'},
        {'key': 'FFmpegMetadata'},
    ],
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([
        'URL'
    ])

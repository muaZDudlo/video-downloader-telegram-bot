import yt_dlp
import os

def download_video(url, output_path):
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        # Download lower quality to keep file size small
        'format': 'best[height<=480][ext=mp4]/best[height<=360][ext=mp4]/worst[ext=mp4]/worst',
        'quiet': False,
        # Strict 200MB limit
        'max_filesize': 200 * 1024 * 1024,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            return filename
    except Exception as e:
        raise Exception(f"Download failed: {str(e)}")

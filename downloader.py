import yt_dlp
import os

def download_video(url, output_path):
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        # Force compatible format for Telegram
        'format': 'bestvideo[ext=mp4][height<=720]+bestaudio[ext=m4a]/best[ext=mp4][height<=720]/best',
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'quiet': False,
        'no_warnings': False,
        # Ensure compatible codec
        'postprocessor_args': [
            '-c:v', 'libx264',  # H.264 video codec
            '-c:a', 'aac',      # AAC audio codec
            '-strict', 'experimental'
        ],
        'max_filesize': 50 * 1024 * 1024,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

            # Ensure the file has .mp4 extension
            if not filename.endswith('.mp4'):
                filename = os.path.splitext(filename)[0] + '.mp4'

            if not os.path.exists(filename):
                raise Exception(f"Downloaded file not found: {filename}")

            return filename
    except Exception as e:
        raise Exception(f"Download failed: {str(e)}")

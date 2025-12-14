# Telegram Video Downloader Bot

A **private Telegram bot** that allows you to download videos from supported platforms using `yt-dlp`. This bot is designed for **educational and personal use only** and is not intended for sharing copyrighted content.

---

## Features

- Telegram bot integration using `python-telegram-bot`
- Downloads videos from YouTube, Facebook, and other supported platforms
- Automatic cleanup of downloaded files after sending
- Easy-to-read code structure for learning and modification
- Cross-platform support (Windows, macOS, Linux)

---



---

## Prerequisites

- Python 3.10 or higher
- Git
- Telegram account
- Telegram bot token (get from [@BotFather](https://t.me/BotFather))

---

## Installation & Setup

1. **Clone the repository** (replace `yourusername` with your GitHub username):

```bash
git clone https://github.video-downloader-telegram-bot.com/yourusername/.git
cd yt-video-downloader-bot
```
2. **Create and activate virtual environment:**

   Linux/macOS-
```bash
python3 -m venv venv
source venv/bin/activate
```
   Windows (PowerShell)-
```bash
python -m venv venv
venv\Scripts\activate
```
3. **Install dependencies:**

```bash
pip install -r requirements.txt
```
4. **Configure environment variables:**
Instead of hardcoding your bot token, create an environment variable:

   Linux/macOS-
```bash
export BOT_TOKEN="YOUR_BOT_TOKEN"
```
   Windows (PowerShell)-
```bash
setx BOT_TOKEN "YOUR_BOT_TOKEN"
```
The bot reads your token from config.py using os.getenv("BOT_TOKEN")


---


## Usage
1. **Run the bot:**
```bash
python bot.py
```
2. **Open Telegram, search for your bot, and send /start to initialize.**

3. **Send a video link (YouTube or Facebook) to the bot.**

4. **The bot will:**

-Download the video

-Send it back as a Telegram video

-Automatically delete the downloaded file from downloads/


---


## Notes & Limitations
1. **Telegram file size limit:** Free bots can send files up to 50MB. Larger videos may fail.

2. **Legal warning:** Only download content you have permission to use. Avoid copyrighted material.

3. **Supported platforms:** Any platform supported by yt-dlp


---


## License

MIT License – for educational use only. See LICENSE file.
   


   
   

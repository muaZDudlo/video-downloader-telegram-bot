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

## Project Structure

video-downloader-telegram-bot/
├── bot.py # Main bot logic
├── downloader.py # Video downloader engine using yt-dlp
├── config.py # Bot configuration (BOT_TOKEN, download folder)
├── requirements.txt# Python dependencies
├── README.md # This file
├── .gitignore # Files/folders to ignore in Git
├── downloads/ # Temporary storage for downloaded videos
│ └── .gitkeep # Keeps the folder in GitHub
└── venv/ # Python virtual environment (NOT pushed)


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
2. 

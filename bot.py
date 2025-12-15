from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from downloader import download_video
from config import BOT_TOKEN, DOWNLOAD_DIR
import os

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Send me a YouTube, Facebook or Instagram video link and I'll download it for you!"
    )

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    msg = await update.message.reply_text("Downloading... ⏳")
    
    try:
        video_path = download_video(url, DOWNLOAD_DIR)
        
        file_size = os.path.getsize(video_path)
        file_size_mb = file_size / (1024 * 1024)
        
        # Check if file is too large for Telegram (2GB limit)
        if file_size > 2000 * 1024 * 1024:
            await msg.edit_text(f"❌ Video is too large ({file_size_mb:.1f}MB). Telegram limit is 2GB.")
            os.remove(video_path)
            return
        
        await msg.edit_text(f"Uploading ({file_size_mb:.1f}MB)... 📤")
        
        # If under 50MB, send as video (playable inline)
        if file_size <= 50 * 1024 * 1024:
            try:
                with open(video_path, 'rb') as video_file:
                    await update.message.reply_video(
                        video=video_file,
                        supports_streaming=True
                    )
            except Exception:
                # Fallback to document if video fails
                with open(video_path, 'rb') as video_file:
                    await update.message.reply_document(
                        document=video_file,
                        caption=f"Video ({file_size_mb:.1f}MB)"
                    )
        else:
            # Send as document for files over 50MB
            with open(video_path, 'rb') as video_file:
                await update.message.reply_document(
                    document=video_file,
                    caption=f"Video ({file_size_mb:.1f}MB) - Too large for inline playback"
                )
        
        os.remove(video_path)
        await msg.delete()
        
    except Exception as e:
        await msg.edit_text(f"❌ Error: {str(e)}")
        if 'video_path' in locals() and os.path.exists(video_path):
            os.remove(video_path)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

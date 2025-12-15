from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from downloader import download_video
from config import BOT_TOKEN, DOWNLOAD_DIR
import os

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Send me a YouTube, Facebook or Instagram video link!\n"
        "Max size: 200MB"
    )

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    msg = await update.message.reply_text("📥 Downloading...")
    
    video_path = None
    
    try:
        video_path = download_video(url, DOWNLOAD_DIR)
        
        file_size = os.path.getsize(video_path)
        file_size_mb = file_size / (1024 * 1024)
        
        # Telegram limit for bots
        if file_size > 200 * 1024 * 1024:  # 200MB
            await msg.edit_text(
                f"❌ Video is too large ({file_size_mb:.1f}MB)\n"
                f"Maximum: 200MB"
            )
            os.remove(video_path)
            return
        
        await msg.edit_text(f"📤 Uploading ({file_size_mb:.1f}MB)...")
        
        # Always send large files as document
        with open(video_path, 'rb') as video_file:
            await update.message.reply_document(
                document=video_file,
                caption=f"📹 Video ({file_size_mb:.1f}MB)",
                read_timeout=300,
                write_timeout=300
            )
        
        os.remove(video_path)
        await msg.delete()
        
    except Exception as e:
        error_msg = str(e)
        
        if "Entity Too Large" in error_msg:
            await msg.edit_text(
                "❌ File too large for Telegram\n"
                "Try a shorter or lower quality video"
            )
        else:
            await msg.edit_text(f"❌ Error: {error_msg}")
        
        if video_path and os.path.exists(video_path):
            os.remove(video_path)

def main():
    app = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .read_timeout(300)
        .write_timeout(300)
        .build()
    )
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))
    
    print(" Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()

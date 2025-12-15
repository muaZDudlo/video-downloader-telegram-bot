from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from downloader import download_video
from config import BOT_TOKEN, DOWNLOAD_DIR
import os

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Send me a YouTube or Facebook video link and I'll download it for you!"
    )

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    msg = await update.message.reply_text("Downloading... ⏳")

    try:
        video_path = download_video(url, DOWNLOAD_DIR)

        file_size = os.path.getsize(video_path)
        if file_size > 50 * 1024 * 1024:
            await msg.edit_text("❌ Video is too large (>50MB).")
            os.remove(video_path)
            return

        await msg.edit_text("Uploading... 📤")

        try:
            # Try sending as video first
            with open(video_path, 'rb') as video_file:
                await update.message.reply_video(
                    video=video_file,
                    supports_streaming=True
                )
        except Exception:
            # If video fails, send as document
            with open(video_path, 'rb') as video_file:
                await update.message.reply_document(
                    document=video_file,
                    caption="Video sent as file"
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

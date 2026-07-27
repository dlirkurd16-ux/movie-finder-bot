
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("8844273487:AAEchHK1TJx3JELYzTFoD55fNVGNLBlJdd8")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\n"
        "لینک یا فایل ویدئو رو بفرست تا بررسی کنم 🎬"
    )


async def video_check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "http" in text:
        await update.message.reply_text(
            "🔍 لینک دریافت شد...\n"
            "در حال بررسی ویدئو هستم..."
        )

        # مرحله بعد: تشخیص فیلم/انیمه با هوش مصنوعی

    else:
        await update.message.reply_text(
            "لطفاً یک لینک ویدئو یا فایل ویدئو ارسال کن."
        )


async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎥 ویدئو دریافت شد.\n"
        "در حال پردازش..."
    )

    # مرحله بعد: تحلیل فریم‌های ویدئو


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, video_check)
    )
    app.add_handler(
        MessageHandler(filters.VIDEO, handle_video)
    )

    print("Bot Started...")
    app.run_polling()


if __name__ == "__main__":
    main()

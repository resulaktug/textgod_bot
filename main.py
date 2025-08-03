from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import os

TOKEN = os.getenv("TOKEN")

def cevaplar(mesaj):
    return [
        "Bıraksın gitsin kral, seni hak etmiyordu zaten.",
        f"Bu mesaj: “{mesaj}” — cevabı hak etmiyor bile 😏",
        "Senin gibi adamın gönlünü kırmak haramdır bro."
    ]

async def start(update, context):
    await update.message.reply_text("Hazırım kral, mesajı yapıştır gel.")

async def mesaj(update, context):
    text = update.message.text
    if "dedi ki" in text.lower():
        yanitlar = cevaplar(text)
        await update.message.reply_text("\n\n".join(yanitlar))
    else:
        await update.message.reply_text("Kız ne dedi? 'Kız dedi ki: ...' yazman lazım.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mesaj))
    app.run_polling()

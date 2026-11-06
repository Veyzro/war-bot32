```python
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import config
import database as db

logging.basicConfig(level=logging.INFO)
ADMIN_ID = 123456789 # بعدا آیدی عددی خودت رو اینجا میذاریم

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    db.add_user(user.id, user.username, user.first_name)
    keyboard = [
        [InlineKeyboardButton("🌍 لیست کشورها", callback_data="list")],
        [InlineKeyboardButton("📰 خبرها", callback_data="news")]
    ]
    await update.message.reply_text(f"سلام {user.first_name} 👋\nبه بازی جنگ جهانی خوش اومدی!", reply_markup=InlineKeyboardMarkup(keyboard))

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "list":
        countries = db.get_countries()
        text = "🌍 لیست کشورها:\n\n"
        for c in countries:
            status = "🔴 رزرو شده" if c[2] else "🟢 آزاد"
            text += f"• {c[1]} — {status}\n"
        if not countries: text += "هنوز کشوری اضافه نشده."
        await query.edit_message_text(text)
        
    elif query.data == "news":
        news = db.get_random_news()
        await query.edit_message_text(f"📰 خبر:\n\n{news}" if news else "هنوز خبری نیست.")

def main():
    db.init_db()
    app = Application.builder().token(config.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
```

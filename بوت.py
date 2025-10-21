from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ضع التوكن الخاص بالبوت هنا
TOKEN = "7808570910:AAF897D7rmaRZDUGcmRcG8Iz7bLreTL2_Yg"

# دالة تتعامل مع أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك في بوت التلجرام!")

# دالة تعيد الرسائل اللي تكتبها للبوت
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

# إعداد التطبيق وال.addHandler
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# تشغيل البوت
app.run_polling()
#
print("تم")
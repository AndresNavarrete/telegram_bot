import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, CallbackContext

from dotenv import find_dotenv, load_dotenv
import os


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def help_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)


if __name__ == '__main__':
    load_dotenv()
    token = os.environ.get("TOKEN")
    application = ApplicationBuilder().token(token).build()

    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)
    
    application.run_polling()
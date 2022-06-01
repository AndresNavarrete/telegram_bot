import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, CallbackContext

from dotenv import find_dotenv, load_dotenv
import os

from messages.help import help_menu, love_msg
from messages.memes import get_meme_url

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def help_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    msg = help_menu()
    await update.message.reply_text(msg)


async def echo(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    default_msg = "Si tienes dudas puedes usar el comando /help ❤️"
    text_input = update.message.text
    text_output = default_msg
    if text_input == '1':
        text_output = love_msg()
    if text_input == '2':
        text_output = get_meme_url()

    await update.message.reply_text(text_output)


if __name__ == '__main__':
    load_dotenv()
    token = os.environ.get("TOKEN")
    application = ApplicationBuilder().token(token).build()

    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)
    
    application.run_polling()
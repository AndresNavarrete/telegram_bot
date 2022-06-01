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
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hola amor! ❤️ Ahora puedes pedirle cosas a nuestro bot")

async def help_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    msg = help_menu()
    await update.message.reply_text(msg)


async def answer(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    text_input = update.message.text
    if text_input == '1':
        await update.message.reply_text(love_msg())

    elif text_input == '2':
        text_output = get_meme_url()
        await update.message.reply_photo(get_meme_url(), caption = "Meme para mi amorcito 💜")

    else:
        default_msg = "Con el comando /help  me puedes dar instrucciones"
        await update.message.reply_text(default_msg)


if __name__ == '__main__':
    load_dotenv()
    token = os.environ.get("TOKEN")
    application = ApplicationBuilder().token(token).build()

    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), answer)
    application.add_handler(message_handler)
    
    application.run_polling()
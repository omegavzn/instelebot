import Constants as keys
from telegram.ext import *
import Responses as R

print("HyphaeBot started...")

def start_command(update, context):
    update.message.reply_text('This is how to get started...')

def help_command(update, context):
    update.message.reply_text('If you need help...')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} causes error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_error_handler(error)

    updater.start_polling(60)
    updater.idle()

main()
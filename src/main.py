import telegram
from telegram.ext import Updater, MessageHandler, Filters
from os import environ

# Replace YOUR_API_TOKEN with your actual API token
token = environ.get('TELEGRAM_HTTP_APIKEY')
bot = telegram.Bot(token=token)

def send_message(chat_id):
    # Replace YOUR_MESSAGE with the message you want to send
    bot.send_message(chat_id=chat_id, text='quien?')

def handle_message(update, context):
    # Replace YOUR_KEYWORD with the word you want to listen for
    invalid_names = ['Aldo', 'Carlos', 'Arreguin', 'Manzano', 'Alvaro']

    if (True if update.message.text in invalid_names else False):
        send_message(update.message.chat_id)

def main():
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    # Handle messages with the handle_message function
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

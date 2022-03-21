import logging
import telegram
from telegram import Update, ForceReply
import telegram.ext 
# import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# def help_command(update: Update, context: CallbackContext) -> None:
#     """Send a message when the command /help is issued."""
#     update.message.reply_text('hello felipe')
# def notas_command(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text('Qual disciplina você quer saber a nota?')

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # updater = Updater("")
    bot = telegram.Bot(token='')
    print(bot.get_me())
    updates = bot.get_updates()
    print(updates[0])
    bot.send_message(text='Hi John!', chat_id=1873831179)
    
    

    # Get the dispatcher to register handlers
    # dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    # dispatcher.add_handler(CommandHandler("help", help_command))
    # dispatcher.add_handler(CommandHandler("notas", notas_command))
    

    # Start the Bot
    # updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    # updater.idle()

if __name__ == '__main__':
    main()
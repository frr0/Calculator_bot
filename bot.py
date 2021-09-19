from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')
    
def solve(update, context) -> None:
  	# /solve 2+2 3+3
    # args = ['2+2', '3+3']
	update.message.reply_text(eval(context.args[0]))

def date(update, context):
    update.message.reply_text(str(datetime.datetime.now()))
    #  update.message.reply_text("e che ne so che data è")

updater = Updater('Token')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.dispatcher.add_handler(CommandHandler('solve', solve))

updater.dispatcher.add_handler(CommandHandler('date', date))

updater.start_polling()
updater.idle()

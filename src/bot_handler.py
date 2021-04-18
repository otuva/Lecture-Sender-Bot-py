"""
todo:
- use credential .txt to check user and bot api
+ script to handle dbs system's lectures
+ logging
"""
from uuid import uuid4
from telegram import Update
from telegram.ext import Updater, CallbackContext
from telegram.ext import CommandHandler
from telegram.error import BadRequest
import logging
import lecture_handler
import sudo_handler

# admin list
# using personal chat id to authenticate risky commands that runs locally.
admin_list = [1000000000]  # change this

log_file = "telegram.log"  # change this

# opening and closing file to append new line to make log look somewhat prettier format-wise.
file = open(log_file, mode='a')
file.write("\n")
file.close()

# starting logger
logging_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename=log_file,
                    filemode='a',
                    format=logging_format,
                    level=logging.INFO
                    )
logger = logging.getLogger(__name__)

# initial interval to display on /start command
interval = 30  # optionally change


# calling this to log function calls
def command_logging(user, command):
    """Log user and command"""
    log = "[FULLNAME: {} | USERNAME: {} | ID: {}] used command '{}'".format(user.full_name,
                                                                            user.username,
                                                                            user.id,
                                                                            command
                                                                            )
    print(log)
    logger.info(log)


# commands
def start(update: Update, context: CallbackContext) -> None:
    """Send a message to /start command"""

    user = update.message.from_user
    command_logging(user, "start")

    update.message.reply_text(
        "Hi! This is Lecture Bot for AtaUni CE\n"
        "It'll check for lectures every {} minutes\n\n"
        "🟢Type /start to see this message\n\n"
        "🟡Type /lec to see today's lectures\n\n"
        "🔵Type /info for more information and the source code\n\n"
        "🔴Authorized only commands:\n"
        "🔴Update lecture list /force\n"
        "🔴Set interval /minute <m>\n".format(interval)
    )


def lec(update: Update, context: CallbackContext) -> None:
    """Display read lectures"""

    user = update.message.from_user
    command_logging(user, "lec")

    file = open("lectures.txt", 'r')
    text = file.read()

    # bot can only handle 4096 bytes per message.
    # if lectures are too long it won't send any message. to solve that sending shortened version of text
    try:
        update.message.reply_text(text)
    except BadRequest:
        error_message = "\n\n🟣There are too many lectures. Displaying shortened version.🟣\n\n"

        text = error_message + text[:3800] + error_message + text[-21:]
        update.message.reply_text(text)

    file.close()


def info(update: Update, context: CallbackContext) -> None:
    """Display more information and source code"""

    user = update.message.from_user
    command_logging(user, "info")

    update.message.reply_text('Soon there will be a link to the source.\n\n'
                              '♤ OAA ♤')


# admin only commands
def force(update: Update, context: CallbackContext) -> None:
    """Force an update on lecture list"""
    user = update.message.from_user

    if user.id in admin_list:
        update.message.reply_text("Updating started.")
        lecture_handler.main()
        update.message.reply_text("Updated.")
        command_logging(user, "force_GRANTED")
    else:
        update.message.reply_text("🚫You don't have permission to do it🚫")
        command_logging(user, "force_DENIED")


def minute(update: Update, context: CallbackContext) -> None:
    global interval
    """Set time interval for update"""
    user = update.message.from_user

    # Generate ID and seperate value from command
    key = str(uuid4())
    # We don't use context.args here, because the value may contain whitespaces
    value = update.message.text.partition(' ')[2]
    # Store value
    context.user_data[key] = value

    if user.id in admin_list:
        # restricting viable minutes to not mess up crontab file
        if value.isdigit() and len(value) == 2:
            value = int(value)
            interval = value

            sudo_handler.main(interval)

            update.message.reply_text("Interval updated to {}.".format(value))
            command_logging(user, "minute_GRANTED_{}".format(value))
        else:
            update.message.reply_text("Invalid value.")
            command_logging(user, "minute_GRANTED_INVALID")
    else:
        update.message.reply_text("🚫You don't have permission to do it🚫")
        command_logging(user, "minute_DENIED")


# main function after the commands
def main():
    # give token and starting updater & dispatcher
    bot_token = '1000000000:AAAAAAA-BBBBBBBBBBBB_CCCCCCCCCCCCCC'  # change this. duh.
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    # adding commands
    start_handler = CommandHandler('start', start)
    lec_handler = CommandHandler('lec', lec)
    info_handler = CommandHandler('info', info)
    force_handler = CommandHandler('force', force)
    minute_handler = CommandHandler('minute', minute)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(lec_handler)
    dispatcher.add_handler(info_handler)
    dispatcher.add_handler(force_handler)
    dispatcher.add_handler(minute_handler)

    # start bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

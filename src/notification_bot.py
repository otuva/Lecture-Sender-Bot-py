from telegram.ext import Updater


def main():
    """message admin if there's a change"""
    # I didn't bother to deep link
    # because the only one will be using notification bot is myself.
    # so why not use another bot to message me if there's, indeed, a change.
    chat_id = 1000000000  # change this

    # give token and starting updater & dispatcher
    reply = "Lecture list is updated.\n" \
            "There is a new lecture."
    bot_token = "1000000000:AAAAAAA-BBBBBBBBBBBB_CCCCCCCCCCCCCC"  # change this
    updater = Updater(token=bot_token, use_context=True)

    updater.bot.sendMessage(chat_id=chat_id, text=reply)


if __name__ == '__main__':
    main()

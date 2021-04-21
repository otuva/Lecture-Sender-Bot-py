# Lecture-Sender-Bot-py
A Telegram bot for reading and indexing lectures from AtaUni CE.

---

[Chat with the bot on Telegram.](https://t.me/lecturesender_bot)

**Usage:**

0- Take a bot token from telegram's _Bot Father_.

1- Change things inside '_CHANGE_THESE.txt_'. 

2- Set up crontab for '_bot_handler.py_' and '_lecture_handler.py_'.

3- Profit.

---

For example you can append code block below to your crontab file. (For Linux.)

_/etc/crontab_
```
#start bot script at reboot
@reboot <USER> cd /home/<USER>/<PATH_TO>/src/; python3 bot_handler.py

#Every 30 minutes, between 07:00 AM and 05:59 PM, Monday through Friday
*/30 7-17 * * 1-5 <USER> cd /home/<USER>/<PATH_TO>/src/; python3 lecture_handler.py
```

---


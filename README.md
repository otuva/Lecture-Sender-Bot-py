# Lecture-Sender-Bot-py

# NOT MAINTAINED 

[![MIT Licence](https://img.shields.io/badge/license-MIT-success.svg)](https://github.com/otuva/Lecture-Sender-Bot-py/blob/main/LICENSE)
[![Repo Size](https://img.shields.io/github/repo-size/otuva/Lecture-Sender-Bot-py)](https://github.com/otuva/Lecture-Sender-Bot-py)

---

[Chat with the bot on Telegram. (~~Online since 24 February 2021~~) **Currently offline.**](https://t.me/lecturesender_bot)

### Usage:

0- Take a bot token from the Telegram's _Bot Father_.

1- Change things inside '_CHANGE_THESE.txt_'. 

2- Set up crontab for '_bot_handler.py_' and '_lecture_handler.py_'.

3- Profit.

---

For example, you can append code block below to your crontab file. (For Linux.)

_/etc/crontab_
```
#start bot script at reboot
@reboot <USER> cd /home/<USER>/<PATH_TO>/src/; python3 bot_handler.py

#Every 30 minutes, between 07:00 AM and 05:59 PM, Monday through Friday
*/30 7-17 * * 1-5 <USER> cd /home/<USER>/<PATH_TO>/src/; python3 lecture_handler.py
```

---

#### Commands:

Command  | Description
------------- | -------------
start  | Start the bot
lec  | List lectures
info | Source link
force | Update list
minute | Change interval

---

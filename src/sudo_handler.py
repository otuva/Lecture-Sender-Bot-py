import os


def main(minute):
    """handle crontab editing permissions"""
    # sudo pasword
    passwd = "pppp"  # change this

    command = "python3 cron_handler.py {}".format(minute)
    os.popen("sudo -S {}".format(command), 'w').write(passwd)


if __name__ == '__main__':
    main(30)

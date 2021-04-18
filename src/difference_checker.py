import notification_bot

def main():
    """checking if lectures are updated"""
    # brute forced the solution it's a mess under here
    # I wouldn't recommend checking it
    file_path = "lectures.txt"  # change this
    cache_path = "cache.txt"  # and this

    file = open(file_path, "r")
    current_length = len(file.read())
    # print(current_length)
    file.close()

    cache_file = open(cache_path, "r")
    cache = cache_file.read().strip()
    cache_file.close()

    cache_file = open(cache_path, "w")

    if current_length == int(cache):
        # print("no changes")
        cache_file.write(str(cache))
        cache_file.close()
    else:
        print("file has changed {}".format(current_length))
        cache_file.write(str(current_length))
        cache_file.close()
        if current_length != 52:

            # I didn't bother to deep link
            # because the only one will be using notification bot is myself.
            # so why not use another bot to message me if there's, indeed, a change.
            notification_bot.main()


if __name__ == '__main__':
    main()


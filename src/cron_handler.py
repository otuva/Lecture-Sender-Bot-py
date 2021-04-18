import sys


def main():
    """using this module to handle /minute command"""
    file = open("/etc/crontab", "r+")

    new_minute = sys.argv[1]
    # current_minute = file.readlines()[-1].split()[0][2:]
    currentfile = file.readlines()

    # read file and edit last line
    last_item_in_current_file = currentfile[-1]
    last_line_in_list = last_item_in_current_file.split()
    last_line_in_list[0] = last_line_in_list[0][0:2] + new_minute
    new_last_line = " ".join(last_line_in_list)

    # change the last line in original file
    currentfile[-1] = new_last_line

    file.seek(0)
    file.writelines(currentfile)

    # print(new_last_line)

    # file.writelines()

    file.close()


main()

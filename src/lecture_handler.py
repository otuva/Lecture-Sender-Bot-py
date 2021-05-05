"""
brute forced solution.
kinda mess but I suppose no one but me would use solution below
different websites would require different solutions
I put this module here only to have complete source code on github
so it's just a specimen module
"""
def main():
    """authenticate and scrape lectures from uni's website"""
    import requests
    import datetime
    import time
    from bs4 import BeautifulSoup
    import difference_checker

    t = datetime.date.today()
    # today in seconds
    # that's how their system works
    mk = int(time.mktime(t.timetuple()))

    # links and credentials to use
    credentials = {'UserName': '11111111111', 'Password': 'pppppp'}
    login_page = "https://obs.atauni.edu.tr/moduller/islem/login/dogrulaKullanici"
    main_page = "https://obs.atauni.edu.tr/moduller/sayfa/info/index"
    sub_page = "https://obs.atauni.edu.tr/moduller/islem/info/DBS"
    calendar_page = "https://dbs.atauni.edu.tr/calendar/view.php?view=day&time={}".format(mk)

    with requests.Session() as session:
        # logging in
        session.post(login_page, data=credentials)
        obs_page = session.get(main_page)
        dbs_page = session.get(sub_page)
        calendar = session.get(calendar_page)
        soup = BeautifulSoup(calendar.content, features='lxml')

    # bs4 formatting
    to_delete = ["\n", "{a} şu tarih için ayarlandı;", "Bugün", "Ders", "olayı", "Etkinliğe git", ",",
                 "Oturuma katıl", "◄", "►", "Gönderim", "ekle"]
    lectures_card = soup.find("div", {'class': 'eventlist my-1'})

    events = lectures_card.text
    for item in to_delete:
        events = events.replace(item, "")

    events = events.split()
    index_list = []
    for item in events:
        if ':' in item:
            if events.index(item) in index_list:
                index_list.append(events.index(item, events.index(item)+1))
            else:
                index_list.append(events.index(item))

    index_list = list(set(index_list))

    index_list.sort(key=int)

    # more formatting
    index_list.append(len(events))
    file = open("lectures.txt", "w")
    if len(index_list) == 1 and "yok." in events:
        file.write("Currently there are no events.\n")
    else:
        for i in range(len(index_list) - 1):
            lecture = events[index_list[i]:index_list[i + 1]]
            lecture.append("➜")
            lecture.append(lecture[0])
            lecture.pop(0)
            file.write(" ".join(lecture) + "\n\n")
    file.write("\n♚L. Check: " + datetime.datetime.now().time().isoformat()[:8] + "\n")
    file.close()

    # call difference checker module
    difference_checker.main()


if __name__ == '__main__':
    main()


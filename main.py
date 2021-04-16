from concurrent.futures import ThreadPoolExecutor
import threading
from urllib import request as req
from urllib import error as er
from fake_useragent import UserAgent
import curses
import os
import time


class PicClass:
    def __init__(self, is_r18, url):
        self.is_r18 = is_r18
        self.url = url


class IllustClass:
    def __init__(self, illust_id, illust_name, pic_class_list):
        self.illust_id = illust_id
        self.illust_name = illust_name
        self.pic_class_list = pic_class_list


# Written in a loop for going through illusts, another loop for all pics of the illust
# pic_class_list_popped for popping operation
# Problem: When writting pics.csv, it writes in illust class. A CLASS IN TOTAL IS NEEDED. 
def get_pic_for_each_illust(illust_class: IllustClass, pic_class: PicClass, pic_class_list_popped: list):
    # Parameters on a larger scpoe than pic_class:
    # pic_num_cnt & pic_numfor all illusts
    global pic_num_cnt, pic_num, conf, pids
    # Get thread id
    pid = threading.get_native_id()
    try:
        r = pids.index(pid)
    except:
        pids.append(pid)
        r = pids.index(pid)
    finally:
        headers = [('User-Agent', UserAgent().random),
                   ('Referer', 'https://www.pixiv.net')]
        opener = req.build_opener()
        opener.addheaders = headers
        req.install_opener(opener)
        downloadName = pic_class.url[57:]
        path0 = "./LSP/" + illust_class.illust_name
        if os.path.exists(path0) == False:
            os.mkdir(path0)
        if pic_class.is_r18:
            path = path0 + "/R/"
        else:
            path = path0 + "/NR/"
        pic_path = path + downloadName
        if not os.path.exists(path):
            os.mkdir(path)
        # 58: len("https://i.pximg.net/img-original/img/2020/12/01/00/01/59/")
        dinfo = '(' + illust_class.illust_name + ')' + pic_class.url[58:]
        stdscr.addstr(r, 36, dinfo)
        try:
            # Enum these threads, supporting up to 16
            if r == 0:
                stdscr.addstr(0, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(0, 0, '[')
                stdscr.addstr(0, 11, ']')
                req.urlretrieve(pic_class.url, pic_path, Emp.downloadBar0)
                stdscr.addstr(0, 0, 66 * ' ')
                stdscr.addstr(0, 0, "Completed.")
            if r == 1:
                stdscr.addstr(1, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(1, 0, '[')
                stdscr.addstr(1, 11, ']')
                req.urlretrieve(pic_class.url, pic_path, Emp.downloadBar1)
                stdscr.addstr(1, 0, 66 * ' ')
                stdscr.addstr(1, 0, "Completed.")
            if r == 2:
                stdscr.addstr(2, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(2, 0, '[')
                stdscr.addstr(2, 11, ']')
                req.urlretrieve(pic_class.url, pic_path, Emp.downloadBar2)
                stdscr.addstr(2, 0, 66 * ' ')
                stdscr.addstr(2, 0, "Completed.")
            if r == 3:
                stdscr.addstr(3, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(3, 0, '[')
                stdscr.addstr(3, 11, ']')
                req.urlretrieve(pic_class.url, pic_path, Emp.downloadBar3)
                stdscr.addstr(3, 0, 66 * ' ')
                stdscr.addstr(3, 0, "Completed.")
            if r == 4:
                stdscr.addstr(4, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(4, 0, '[')
                stdscr.addstr(4, 11, ']')
                req.urlretrieve(pic_class.url, pic_path, Emp.downloadBar4)
                stdscr.addstr(4, 0, 66 * ' ')
                stdscr.addstr(4, 0, "Completed.")
            if r == 5:
                stdscr.addstr(5, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(5, 0, '[')
                stdscr.addstr(5, 11, ']')
                req.urlretrieve(pic_class.url, pic_path, Emp.downloadBar5)
                stdscr.addstr(5, 0, 66 * ' ')
                stdscr.addstr(5, 0, "Completed.")
            if r == 6:
                stdscr.addstr(6, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(6, 0, '[')
                stdscr.addstr(6, 11, ']')
                req.urlretrieve(pic_class.url, pic_path, Emp.downloadBar6)
                stdscr.addstr(6, 0, 66 * ' ')
                stdscr.addstr(6, 0, "Completed.")
            if r == 7:
                stdscr.addstr(7, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(7, 0, '[')
                stdscr.addstr(7, 11, ']')
                req.urlretrieve(pic_class.url, pic_path, Emp.downloadBar7)
                stdscr.addstr(7, 0, 66 * ' ')
                stdscr.addstr(7, 0, "Completed.")
            if r == 8:
                stdscr.addstr(8, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(8, 0, '[')
                stdscr.addstr(8, 11, ']')
                req.urlretrieve(pic_class.url, pic_path, Emp.downloadBar8)
                stdscr.addstr(8, 0, 66 * ' ')
                stdscr.addstr(8, 0, "Completed.")
            if r == 9:
                stdscr.addstr(9, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(9, 0, '[')
                stdscr.addstr(9, 11, ']')
                req.urlretrieve(pic_class.url, pic_path, Emp.downloadBar9)
                stdscr.addstr(9, 0, 66 * ' ')
                stdscr.addstr(9, 0, "Completed.")
            if r == 10:
                stdscr.addstr(10, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(10, 0, '[')
                stdscr.addstr(10, 11, ']')
                req.urlretrieve(pic_class.url, pic_path, Emp.downloadBar10)
                stdscr.addstr(10, 0, 66 * ' ')
                stdscr.addstr(10, 0, "Completed.")
            if r == 11:
                stdscr.addstr(11, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(11, 0, '[')
                stdscr.addstr(11, 11, ']')
                req.urlretrieve(pic_class.url, pic_path, Emp.downloadBar11)
                stdscr.addstr(11, 0, 66 * ' ')
                stdscr.addstr(11, 0, "Completed.")
            if r == 12:
                stdscr.addstr(12, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(12, 0, '[')
                stdscr.addstr(12, 11, ']')
                req.urlretrieve(pic_class.url, pic_path, Emp.downloadBar12)
                stdscr.addstr(12, 0, 66 * ' ')
                stdscr.addstr(12, 0, "Completed.")
            if r == 13:
                stdscr.addstr(13, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(13, 0, '[')
                stdscr.addstr(13, 11, ']')
                req.urlretrieve(pic_class.url, pic_path, Emp.downloadBar13)
                stdscr.addstr(13, 0, 66 * ' ')
                stdscr.addstr(13, 0, "Completed.")
            if r == 14:
                stdscr.addstr(14, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(14, 0, '[')
                stdscr.addstr(14, 11, ']')
                req.urlretrieve(pic_class.url, pic_path, Emp.downloadBar14)
                stdscr.addstr(14, 0, 66 * ' ')
                stdscr.addstr(14, 0, "Completed.")
            if r == 15:
                stdscr.addstr(15, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(15, 0, '[')
                stdscr.addstr(15, 11, ']')
                req.urlretrieve(pic_class.url, pic_path, Emp.downloadBar15)
                stdscr.addstr(15, 0, 66 * ' ')
                stdscr.addstr(15, 0, "Completed.")
            for i in range(len(pic_class_list_popped)):
                if pic_class_list_popped[i].url == pic_class.url:
                    pic_class_list_popped.pop(i)
                    break
            # Historical problem
            with open("./pics.csv", "w+", encoding='utf-8') as list_of_pics:
                #pic_class_for_loop: PicClass
                for pic_class_for_loop in pic_class_list_popped:
                    istr = str(pic_class_for_loop.is_r18) + ',' + pic_class_for_loop.url + \
                        ',' + illust_class.illust_name + '\n'
                    list_of_pics.write(istr)
                list_of_pics.close()
            pic_num_cnt += 1
            totalper = "%.2f" % (pic_num_cnt / pic_num * 100)
            stdscr.addstr(16, 0, "Total progress:" + str(pic_num_cnt) +
                          '/' + str(pic_num) + ', ' + str(totalper) + r'%')
            stdscr.refresh()

        except er.HTTPError as her:

            if her.code == 404:
                for i in range(len(pic_class_list_popped)):
                    if pic_class_list_popped[i].url == pic_class.url:
                        pic_class_list_popped.pop(i)
                        break
                with open("./pics.csv", "w+") as list_of_pics:
                    for pic_class_for_loop in pic_class_list_popped:
                        istr = str(pic_class_for_loop.is_r18) + ',' + pic_class_for_loop.url + \
                            ',' + illust_class.illust_name + '\n'
                        list_of_pics.write(istr)
            else:
                raise her


# MIND OUT THE DYNAMIC LIST INDEX!!!
def multithread_illusts(stdscr, threads: int):
    # stdscr: silent parameter
    pool = ThreadPoolExecutor(max_workers=threads)
    illust_num = len(illust_class_list)
    pic_class_list_popped = []
    for i in range(illust_num):
        for pic_class in illust_class_list[i].pic_class_list:
            pic_class_list_popped.append(pic_class)
        # Get a manual copy of pic_class_list to pop
    for i in range(illust_num):
        for j in range(len(illust_class_list[i].pic_class_list)):
            pool.submit(get_pic_for_each_illust, illust_class_list[i], illust_class_list[i].pic_class_list[j], pic_class_list_popped)
    pool.shutdown()




if not os.path.exists('./LSP'):
    os.mkdir('./LSP')
conf = input(
    "Continue last time's downloading[c], start a new one(default), or enlarge the database[e]?")
if conf == 'e':
    from picsDataConfig import f1_picsdata
    from picsDataExec import WriteIllustCSV, WriteRawCSV, ChooseIllust, StaticWritePingCSV, ReadPingCSV
else:
    if conf == 'c':
        from cdl import illust_class_list
    else:
        from eurl import illust_class_list
    stdscr = curses.initscr()
    stdscr.clear()
    stdscr.refresh()
    stdscr.move(0, 0)
    pic_num = 0
    pic_num_cnt = 0
    for illust_class in illust_class_list:
        pic_num += len(illust_class.pic_class_list)
    pic_num /= 2
    pic_num = int(pic_num)

if conf != 'e':
    pids = []
    curses.curs_set(False)

if __name__ == "__main__":
    if conf == 'e':
        if f1_picsdata == '1':
            from eurl import illust_class_list, stdscr
            stdscr.clear()
            stdscr.refresh()
            stdscr.move(0, 0)
            WriteIllustCSV(stdscr, illust_class_list)
            WriteRawCSV(stdscr, illust_class_list)
            # So far, It seems successful.
        elif f1_picsdata == '2':
            stdscr = curses.initscr()
            illust_name_list = ChooseIllust(stdscr)
            stdscr.clear()
            stdscr.addstr(0, 0, "How many threads do you want to work with?\n")
            stdscr.addstr("If there are more than 8 threads, the program will automatically rerun once.\n")
            threads = int(bytes.decode(stdscr.getstr()))
            curses.wrapper(StaticWritePingCSV, illust_name_list, threads)
            # Give another try if threads are too much, for missing chance inceases.
            if threads > 8:
                curses.wrapper(StaticWritePingCSV, illust_name_list, threads)
        elif f1_picsdata == '3':
            import enumProcess as Emp
            stdscr = curses.initscr()
            illust_name_list = ChooseIllust(stdscr)
            illust_class_list = ReadPingCSV(stdscr, illust_name_list)
            stdscr.clear()
            stdscr.addstr(0, 0, "How many threads do you want to work with?\n")
            threads = int(bytes.decode(stdscr.getstr()))
            pic_num = 0
            pic_num_cnt = 0
            for illust_class in illust_class_list:
                pic_num += len(illust_class.pic_class_list)
            pic_num = int(pic_num)
            pids = []
            stdscr.clear()
            stdscr.refresh()
            curses.wrapper(multithread_illusts, threads)
        elif f1_picsdata == '4' or f1_picsdata == '':
            from eurl import illust_class_list, stdscr
            illust_name_list = []
            for illust_class in illust_class_list:
                illust_name_list.append(illust_class.illust_name)
            stdscr.clear()
            stdscr.refresh()
            stdscr.move(0, 0)
            WriteIllustCSV(stdscr, illust_class_list)
            WriteRawCSV(stdscr, illust_class_list)
            stdscr.addstr(0, 0, "How many threads do you want to work with?\n")
            stdscr.addstr("If there are more than 8 threads, the program will automatically rerun once.\n")
            threads = int(bytes.decode(stdscr.getstr()))
            curses.wrapper(StaticWritePingCSV, illust_name_list, threads)
            # Give another try if threads are too much, for missing chance inceases.
            if threads > 8:
                curses.wrapper(StaticWritePingCSV, illust_name_list, threads)
        elif f1_picsdata == '5':
            import enumProcess as Emp
            stdscr = curses.initscr()
            illust_name_list = ChooseIllust(stdscr)
            stdscr.clear()
            stdscr.addstr(0, 0, "How many threads do you want to work with?\n")
            stdscr.addstr("If there are more than 8 threads, the program will automatically rerun once.\n")
            threads = int(bytes.decode(stdscr.getstr()))
            curses.wrapper(StaticWritePingCSV, illust_name_list, threads)
            # Give another try if threads are too much, for missing chance inceases.
            if threads > 8:
                curses.wrapper(StaticWritePingCSV, illust_name_list, threads)
            illust_class_list = ReadPingCSV(stdscr, illust_name_list)
            stdscr.clear()
            stdscr.addstr(0, 0, "How many threads do you want to work with?\n")
            threads = int(bytes.decode(stdscr.getstr()))
            pic_num = 0
            pic_num_cnt = 0
            for illust_class in illust_class_list:
                pic_num += len(illust_class.pic_class_list)
            pic_num = int(pic_num)
            pids = []
            stdscr.clear()
            stdscr.refresh()
            curses.wrapper(multithread_illusts, threads)
        elif f1_picsdata == '6':
            from eurl import stdscr, illust_class_list
            import enumProcess as Emp
            illust_name_list = []
            for illust_class in illust_class_list:
                illust_name_list.append(illust_class.illust_name)
            stdscr.clear()
            stdscr.refresh()
            stdscr.move(0, 0)
            WriteIllustCSV(stdscr, illust_class_list)
            WriteRawCSV(stdscr, illust_class_list)
            stdscr.addstr(0, 0, "How many threads do you want to work with?\n")
            stdscr.addstr("If there are more than 8 threads, the program will automatically rerun once.\n")
            threads = int(bytes.decode(stdscr.getstr()))
            curses.wrapper(StaticWritePingCSV, illust_name_list, threads)
            # Give another try if threads are too much, for missing chance inceases.
            if threads > 8:
                curses.wrapper(StaticWritePingCSV, illust_name_list, threads)
            illust_name_list = ChooseIllust(stdscr)
            illust_class_list = ReadPingCSV(stdscr, illust_name_list)
            stdscr.clear()
            stdscr.addstr(0, 0, "How many threads do you want to work with?\n")
            threads = int(bytes.decode(stdscr.getstr()))
            pic_num = 0
            pic_num_cnt = 0
            for illust_class in illust_class_list:
                pic_num += len(illust_class.pic_class_list)
            pic_num = int(pic_num)
            pids = []
            stdscr.clear()
            stdscr.refresh()
            curses.wrapper(multithread_illusts, threads)
        stdscr.clear()
        if f1_picsdata == '3' or f1_picsdata == '5' or f1_picsdata == '6':
            stdscr.addstr(str(pic_num) + " PICS WERE IN. CHECK THEM OUT!")
        stdscr.addstr("Complete. Press any key to continue...\n")
        stdscr.getch()            
    else:
        import enumProcess as Emp
        with open("./pics.csv", "w+", encoding="utf-8") as picsList:
            for illust_class in illust_class_list:
                for pic_class in illust_class.pic_class_list:
                    istr = str(pic_class.is_r18) + ',' + pic_class.url + \
                        ',' + illust_class.illust_name + '\n'
                    picsList.write(istr)
            picsList.close()
        curses.wrapper(multithread_illusts, 16)
        print("DOWNLOAD FINISHED.")
        print(str(pic_num) + " PICS WERE IN. CHECK THEM OUT!")
        print("DON'T FORGET TO MANUALLY QUIT THE EDGE PROCESS!")

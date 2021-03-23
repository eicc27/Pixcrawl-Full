from concurrent.futures import ThreadPoolExecutor
import threading
from urllib import request as req
from urllib import error as er
from fake_useragent import UserAgent
import curses
import os
import time


class picUrl:
    def __init__(self, isR18, url, illustName):
        self.isR18 = isR18
        self.url = url
        self.illustName = illustName


def wrap(picUrlInClass):
    curses.wrapper(getPic, picUrlInClass)


def getPic(stdscr, picUrlInClass):
    global picNumCnt, picNum, urls
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
        downloadName = picUrlInClass.url[57:]
        path0 = "./LSP/" + picUrlInClass.illustName
        if os.path.exists(path0) == False:
            os.mkdir(path0)
        if picUrlInClass.isR18 == True:
            path = path0 + "/R/"
        else:
            path = path0 + "/NR/"
        picPath = path + downloadName
        if os.path.exists(path) == False:
            os.mkdir(path)
        try:

            if r == 0:
                stdscr.addstr(0, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(0, 0, '[')
                stdscr.addstr(0, 11, ']')
                req.urlretrieve(picUrlInClass.url, picPath, emp.downloadBar0)
                stdscr.addstr(0, 0, 40 * ' ')
                stdscr.addstr(0, 0, "Completed.")
            if r == 1:
                stdscr.addstr(1, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(1, 0, '[')
                stdscr.addstr(1, 11, ']')
                req.urlretrieve(picUrlInClass.url, picPath, emp.downloadBar1)
                stdscr.addstr(1, 0, 40 * ' ')
                stdscr.addstr(1, 0, "Completed.")
            if r == 2:
                stdscr.addstr(2, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(2, 0, '[')
                stdscr.addstr(2, 11, ']')
                req.urlretrieve(picUrlInClass.url, picPath, emp.downloadBar2)
                stdscr.addstr(2, 0, 40 * ' ')
                stdscr.addstr(2, 0, "Completed.")
            if r == 3:
                stdscr.addstr(3, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(3, 0, '[')
                stdscr.addstr(3, 11, ']')
                req.urlretrieve(picUrlInClass.url, picPath, emp.downloadBar3)
                stdscr.addstr(3, 0, 40 * ' ')
                stdscr.addstr(3, 0, "Completed.")
            if r == 4:
                stdscr.addstr(4, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(4, 0, '[')
                stdscr.addstr(4, 11, ']')
                req.urlretrieve(picUrlInClass.url, picPath, emp.downloadBar4)
                stdscr.addstr(4, 0, 40 * ' ')
                stdscr.addstr(4, 0, "Completed.")
            if r == 5:
                stdscr.addstr(5, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(5, 0, '[')
                stdscr.addstr(5, 11, ']')
                req.urlretrieve(picUrlInClass.url, picPath, emp.downloadBar5)
                stdscr.addstr(5, 0, 40 * ' ')
                stdscr.addstr(5, 0, "Completed.")
            if r == 6:
                stdscr.addstr(6, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(6, 0, '[')
                stdscr.addstr(6, 11, ']')
                req.urlretrieve(picUrlInClass.url, picPath, emp.downloadBar6)
                stdscr.addstr(6, 0, 40 * ' ')
                stdscr.addstr(6, 0, "Completed.")
            if r == 7:
                stdscr.addstr(7, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(7, 0, '[')
                stdscr.addstr(7, 11, ']')
                req.urlretrieve(picUrlInClass.url, picPath, emp.downloadBar7)
                stdscr.addstr(7, 0, 40 * ' ')
                stdscr.addstr(7, 0, "Completed.")
            if r == 8:
                stdscr.addstr(8, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(8, 0, '[')
                stdscr.addstr(8, 11, ']')
                req.urlretrieve(picUrlInClass.url, picPath, emp.downloadBar8)
                stdscr.addstr(8, 0, 40 * ' ')
                stdscr.addstr(8, 0, "Completed.")
            if r == 9:
                stdscr.addstr(9, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(9, 0, '[')
                stdscr.addstr(9, 11, ']')
                req.urlretrieve(picUrlInClass.url, picPath, emp.downloadBar9)
                stdscr.addstr(9, 0, 40 * ' ')
                stdscr.addstr(9, 0, "Completed.")
            if r == 10:
                stdscr.addstr(10, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(10, 0, '[')
                stdscr.addstr(10, 11, ']')
                req.urlretrieve(picUrlInClass.url, picPath, emp.downloadBar10)
                stdscr.addstr(10, 0, 40 * ' ')
                stdscr.addstr(10, 0, "Completed.")
            if r == 11:
                stdscr.addstr(11, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(11, 0, '[')
                stdscr.addstr(11, 11, ']')
                req.urlretrieve(picUrlInClass.url, picPath, emp.downloadBar11)
                stdscr.addstr(11, 0, 40 * ' ')
                stdscr.addstr(11, 0, "Completed.")
            if r == 12:
                stdscr.addstr(12, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(12, 0, '[')
                stdscr.addstr(12, 11, ']')
                req.urlretrieve(picUrlInClass.url, picPath, emp.downloadBar12)
                stdscr.addstr(12, 0, 40 * ' ')
                stdscr.addstr(12, 0, "Completed.")
            if r == 13:
                stdscr.addstr(13, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(13, 0, '[')
                stdscr.addstr(13, 11, ']')
                req.urlretrieve(picUrlInClass.url, picPath, emp.downloadBar13)
                stdscr.addstr(13, 0, 40 * ' ')
                stdscr.addstr(13, 0, "Completed.")
            if r == 14:
                stdscr.addstr(14, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(14, 0, '[')
                stdscr.addstr(14, 11, ']')
                req.urlretrieve(picUrlInClass.url, picPath, emp.downloadBar14)
                stdscr.addstr(14, 0, 40 * ' ')
                stdscr.addstr(14, 0, "Completed.")
            if r == 15:
                stdscr.addstr(15, 0, 10 * ' ')
                stdscr.refresh()
                stdscr.addstr(15, 0, '[')
                stdscr.addstr(15, 11, ']')
                req.urlretrieve(picUrlInClass.url, picPath, emp.downloadBar15)
                stdscr.addstr(15, 0, 40 * ' ')
                stdscr.addstr(15, 0, "Completed.")
            urls.pop(urls.index(picUrlInClass))
            with open("./pics.csv", "w+") as picsList:
                for url in urls:
                    istr = str(url.isR18) + ',' + url.url + \
                        ',' + url.illustName + '\n'
                    picsList.write(istr)
            picNumCnt += 1
            totalper = "%.2f" % (picNumCnt / picNum * 100)
            stdscr.addstr(16, 0, "Total progress:" + str(picNumCnt) +
                          '/' + str(picNum) + ', ' + str(totalper) + r'%')
            stdscr.refresh()

        except er.HTTPError as her:

            if her.code == 404:
                urls.pop(urls.index(picUrlInClass))
                with open("./pics.csv", "w+") as picsList:
                    for url in urls:
                        istr = str(url.isR18) + ',' + url.url + \
                            ',' + url.illustName + '\n'
                        picsList.write(istr)

            else:
                stdscr.addstr(0, r, "DOWNLOAD FAILED!!")
                stdscr.refresh()
                time.sleep(5)


conf = input("Continue last time's downloading, or start a new one?")
if conf == 'Y' or conf == 'y' or conf == '':
    from cdl import ourls
    urls = ourls

else:
    from eurl import picUrlsInList
    urls = picUrlsInList


pids = []
stdscr = curses.initscr()
curses.curs_set(False)
picNumCnt = 0
picNum = int(len(urls) / 2)
if __name__ == "__main__":
    import enumProcess as emp
    with open("./pics.csv", "w+") as picsList:
        for url in urls:
            istr = str(url.isR18) + ',' + url.url + \
                ',' + url.illustName + '\n'
            picsList.write(istr)
    pool = ThreadPoolExecutor(max_workers=16)
    for i in range(len(urls)):
        pool.submit(wrap, urls[i])
    pool.shutdown()
    print("DOWNLOAD FINISHED.")
    print(str(picNum) + " PICS WERE IN. CHECK THEM OUT!")
    print("DON'T FORGET TO MANUALLY QUIT THE EDGE PROCESS!")

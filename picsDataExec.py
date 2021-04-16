import os
import threading
from fake_useragent import UserAgent
from urllib import request as req
from urllib import error as er
from time import sleep
# Use multithreading in main
from concurrent.futures import ThreadPoolExecutor
# It's like an API
# It's very rude querying the whole csv, O(n^2)!!
# In algorithm, just a simple search


class IllustClass:
    def __init__(self, illust_id, illust_name, pic_class_list):
        self.illust_id = illust_id
        self.illust_name = illust_name
        self.pic_class_list = pic_class_list


class PicClass:
    def __init__(self, is_r18, url):
        self.is_r18 = is_r18
        self.url = url


class IllustClass:
    def __init__(self, illust_id, illust_name, pic_class_list):
        self.illust_id = illust_id
        self.illust_name = illust_name
        self.pic_class_list = pic_class_list

# filename: 'ping' or 'raw'
def CSVLineCnt(filename: str, illust_name: str) -> int:
    try:
        with open('./PicsDatabase/' + illust_name + '/' + filename + '.csv', 'r', encoding='utf-8') as fstream:
            if fstream.readline() == '':
                return 0
            fstream.seek(0, 0)
            return sum(line.count('\n') for line in fstream.read()) - 1
    except FileNotFoundError:
        return 0


def WriteIllustCSV(stdscr, illust_class_list: list):
    if not os.path.exists("./PicsDatabase/"):
        os.mkdir("./PicsDatabase/")
    with open("./PicsDatabase/illusts.csv", "a+", encoding="utf-8") as illust_stream:
        # When opening with a+, the previous content of file is kept.
        # HOWEVER, the *FILE is at SEEK_END. It must be initialized to SEEK_SET first.
        illust_stream.seek(0, 0)
        illust_header = "illust,ID\n"
        illust_num = len(illust_class_list)
        if illust_stream.readline() == '':
            illust_stream.write(illust_header)
            for i in range(illust_num):
                illust_stream.write(
                    illust_class_list[i].illust_name + "," + illust_class_list[i].illust_id + '\n')
                stdscr.addstr("Illust" + illust_class_list[i].illust_name +
                              "(" + illust_class_list[i].illust_id + ") has been added.")
        else:
            saved_illust_list = illust_stream.readlines()
            saved_illust_num = len(saved_illust_list)
            new_illust_num = 0
            for i in range(illust_num):
                index = 0
                for j in range(saved_illust_num):
                    saved_illust_id = saved_illust_list[j][saved_illust_list[j].rfind(
                        ",") + 1:len(saved_illust_list[j]) - 1]
                    if illust_class_list[i].illust_id == saved_illust_id:
                        break
                    index += 1
                if index == saved_illust_num:
                    new_illust_num += 1
                    illust_stream.seek(0, 2)
                    illust_stream.write(
                        illust_class_list[i].illust_name + "," + illust_class_list[i].illust_id + "\n")
                    stdscr.addstr(
                        "Illust " + illust_class_list[i].illust_name + "(" + illust_class_list[i].illust_id + ") has been newly added.")
            if new_illust_num == 0:
                stdscr.addstr("No new illusts.")
        illust_stream.close()


def WriteRawCSV(stdscr, illust_class_list: list):
    if not os.path.exists("./PicsDatabase/"):
        os.mkdir("./PicsDatabase/")
    for i in range(len(illust_class_list)):
        stdscr.addstr("Writing for illust " +
                      illust_class_list[i].illust_name + ".")
        if not os.path.exists("./PicsDatabase/" + illust_class_list[i].illust_name):
            os.mkdir("./PicsDatabase/" + illust_class_list[i].illust_name)
        with open("./PicsDatabase/" + illust_class_list[i].illust_name + "/raw.csv", "a+", encoding="utf-8") as rawstream:
            # Simply MIND OUT like above.
            rawstream.seek(0, 0)
            crawledlen = len(illust_class_list[i].pic_class_list)
            if rawstream.readline() == '':
                colheader = "url,isR18\n"
                rawstream.write(colheader)
                for j in range(crawledlen):
                    rawstream.write(
                        illust_class_list[i].pic_class_list[j].url + "," + str(illust_class_list[i].pic_class_list[j].is_r18) + '\n')
                finstr = "Writing for illust " + \
                    illust_class_list[i].illust_name + "(" + illust_class_list[i].illust_id + \
                    ") complete, including " + str(crawledlen) + " new urls."
            else:
                pics_in_csv = rawstream.readlines()
                picslen = len(pics_in_csv)
                lendiff = crawledlen - picslen
                if lendiff > 0:
                    finstr = "Writing for illust " + \
                        illust_class_list[i].illust_name + "(" + illust_class_list[i].illust_id + \
                        ") complete, including " + str(lendiff) + " new urls."
                    for j in range(0, crawledlen, 2):
                        if lendiff > 0:
                            index = 0
                            for k in range(0, picslen, 2):
                                picsUrl = pics_in_csv[k][:pics_in_csv[k].rfind(
                                    ',')]
                                if illust_class_list[i].pic_class_list[j].url == picsUrl:
                                    break
                                index += 2
                            if index == picslen:
                                rawstream.seek(0, 2)
                                rawstream.write(
                                    illust_class_list[i].pic_class_list[j].url + "," + str(illust_class_list[i].pic_class_list[j].is_r18) + '\n')
                                rawstream.write(
                                    illust_class_list[i].pic_class_list[j+1].url + "," + str(illust_class_list[i].pic_class_list[j+1].is_r18) + '\n')
                                lendiff -= 2
                else:
                    finstr = "No new urls has been written for " + \
                        illust_class_list[i].illust_name + \
                        "(" + illust_class_list[i].illust_id + ")."
            rawstream.close()
        stdscr.addstr(finstr)


# Static: without a class
# returns a list of illust_name, corresponding to illust_id
def StaticIllustIDLink(stdscr, illust_id_list: list):
    # If the file is deleted, an exception will thrown.
    with open("./PicsDatabase/illusts.csv", "r+", encoding="utf-8") as illust_stream:
        illust_name_list = []
        finstr = "Successfully linked:\n"
        # Move *FILE to the second line
        # Static
        illust_stream.readline()
        saved_illust_list = illust_stream.readlines()
        for illust_id in illust_id_list:
            finstr += illust_id + " "
            saved_illust_num = len(saved_illust_list)
            index = 0
            for i in range(saved_illust_num):
                saved_illust_id = saved_illust_list[i][saved_illust_list[i].rfind(
                    ",") + 1:len(saved_illust_list[i]) - 1]
                if illust_id == saved_illust_id:
                    illust_name_list.append(
                        saved_illust_list[i][:saved_illust_list[i].rfind(",")])
                    break
                index += 1
            if index == saved_illust_num:
                illust_stream.close()
                stdscr.addstr("Link failed.\n")
                stdscr.refresh()
                return []
        illust_stream.close()
        finstr += "\nwith:\n"
        for illust_name in illust_name_list:
            finstr += illust_name
        stdscr.addstr(finstr + '\n')
        stdscr.refresh()
        return illust_name_list


def ChooseIllust(stdscr) -> list:
    stdscr.clear()
    stdscr.refresh()
    stdscr.move(0, 0)
    input_key = True
    while input_key:
        stdscr.addstr(
            "Choose present illustrators from the PicsDatabase folder.\n")
        stdscr.addstr(
            "Use IDs instead of names. If you forgot the IDs, you can query them in the illusts.csv.\n")
        illust_input = bytes.decode(stdscr.getstr())
        illust_id_list = []
        illust_input = illust_input.replace(' ', '')
        illust_input = illust_input.rstrip(',')
        while illust_input.find(',') != -1:
            pos = illust_input.find(',')
            illust_id_list.append(illust_input[0:pos])
            illust_input = illust_input[pos + 1:]
        illust_id_list.append(illust_input)
        illust_name_list = StaticIllustIDLink(stdscr, illust_id_list)
        stdscr.addstr("Press any key to continue...\n")
        stdscr.getch()
        if(len(illust_name_list) == 0):
            stdscr.clear()
            stdscr.refresh()
            stdscr.move(0, 0)
            stdscr.addstr(
                "At least one of the illust ID cannot be identified. Please retype.\n")
        else:
            input_key = False
    return illust_name_list


# Firstly a single-threaded version
# Multithreading needs firstly figuring out what pop is, and how to use len() properly.
# This single function only recieves .jpg file for order reasons, as long as index is an odd.
pids = []
total = 0
downloaded = 0

def StaticSingleWritePingCSV(stdscr, illust_name: str, raw_url_class_list: list, index: int, threads: int):
    global downloaded, total
    pid = threading.get_native_id()
    try:
        r = pids.index(pid)
    except:
        pids.append(pid)
        r = pids.index(pid)
    finally:
        # Rewrite FILE I/O Stream
        with open("./PicsDatabase/" + illust_name + "/ping.csv", "a+", encoding="utf-8") as ping_stream:
            ping_stream.seek(0, 2)
            try:
                # if .jpg works
                stdscr.addstr(
                    r, 0, raw_url_class_list[index].url.rstrip('.jpg')[58:])
                stdscr.refresh()
                req.urlopen(raw_url_class_list[index].url)
                ping_stream.write(
                    raw_url_class_list[index].url + ',' + raw_url_class_list[index].is_r18 + '\n')
            except er.HTTPError as her:
                # then .png works
                if her.code == 404:
                    ping_stream.write(
                        raw_url_class_list[index + 1].url + ',' + raw_url_class_list[index + 1].is_r18 + '\n')
                else:
                    raise her
            stdscr.addstr(r, 10, 2 * ' ')
            ping_stream.close()
            downloaded += 1
            percent = "%.2f" % (downloaded / total * 100)
            stdscr.addstr(threads, 0, str(downloaded) + '/' +
                          str(total) + ', ' + percent + '%')
            stdscr.refresh()

# Note that .jpg & .png are reverse, if one fails the other must be successful.
# Without webdriver, the difference cannot be known, so it's static.


def StaticWritePingCSV(stdscr, illust_name_list: list, threads: int):
    stdscr.clear()
    global pids, total, downloaded
    pids = []
    downloaded = 0
    pool = ThreadPoolExecutor(max_workers=threads)
    # Calculate total first
    rawlines = 0
    pinglines = 0
    for illust_name in illust_name_list:
        rawlines += CSVLineCnt('raw', illust_name)
        pinglines += CSVLineCnt('ping', illust_name)
    total = int(rawlines / 2) - pinglines
    for illust_name in illust_name_list:
        raw_url_class_list = []
        with open("./PicsDatabase/" + illust_name + "/raw.csv", "a+", encoding="utf-8") as raw_stream:
            raw_stream.seek(0, 0)
            raw_stream.readline()
            raw_url_integrated_list = raw_stream.readlines()
            for raw_url_integrated in raw_url_integrated_list:
                # When stored in csv, the front one is url, but when stored in class, the front one is is_r18.
                raw_url_class_list.append(PicClass(raw_url_integrated[raw_url_integrated.rfind(",") + 1:len(
                    raw_url_integrated) - 1], raw_url_integrated[:raw_url_integrated.rfind(",")]))
            raw_stream.close()
        if(len(raw_url_class_list)) == 0:
            pool.shutdown()
            return
        with open("./PicsDatabase/" + illust_name + "/ping.csv", "a+", encoding="utf-8") as ping_stream:
            ping_stream.seek(0, 0)
            ping_stream_header = "url,is_r18\n"
            headers = [('User-Agent', UserAgent().random),
                       ('Referer', 'https://www.pixiv.net')]
            opener = req.build_opener()
            opener.addheaders = headers
            req.install_opener(opener)
            # static int
            raw_url_num = len(raw_url_class_list)
            if ping_stream.readline() == '':
                ping_stream.seek(0, 0)
                ping_stream.write(ping_stream_header)
                for i in range(0, raw_url_num, 2):
                    pool.submit(StaticSingleWritePingCSV, stdscr, illust_name,
                                raw_url_class_list, i, threads)
                    #StaticSingleWritePingCSV(raw_url_class_list, i, ping_stream)
            # If the file has been in existence, compare the longer raw one with the pinged one.
            # Then if matched, pop both of the files out of raw list.
            else:
                ping_url_list = ping_stream.readlines()
                ping_url_num = len(ping_url_list)
                if ping_url_num == 0:
                    for i in range(0, raw_url_num, 2):
                        pool.submit(StaticSingleWritePingCSV, stdscr, illust_name,
                                    raw_url_class_list, i, threads)
                else:
                    raw_url_num = len(raw_url_class_list)
                    lendiff = int(raw_url_num / 2) - ping_url_num
                    if lendiff > 0:
                        pop_index_list = []
                        for i in range(ping_url_num):
                            ping_url = ping_url_list[i][:ping_url_list[i].rfind(
                                ",")]
                            for j in range(raw_url_num):
                                if ping_url == raw_url_class_list[j].url:
                                    if ping_url.find(".jpg") != -1:
                                        pop_index_list.append(j)
                                        pop_index_list.append(j + 1)
                                    else:
                                        pop_index_list.append(j - 1)
                                        pop_index_list.append(j)
                                    break
                        # Default: from small to big
                        pop_index_list.sort()
                        bias = 0
                        for pop_index in pop_index_list:
                            raw_url_class_list.pop(pop_index - bias)
                            bias += 1
                        remaining_url_class_num = len(raw_url_class_list)
                        # If few, go single-threaded
                        if lendiff <= 5:
                            for i in range(0, remaining_url_class_num, 2):
                                StaticSingleWritePingCSV(stdscr, illust_name, 
                                    raw_url_class_list, i, threads)
                        # Else, go multi-threaded
                        else:
                            for i in range(0, remaining_url_class_num, 2):
                                pool.submit(StaticSingleWritePingCSV,stdscr, illust_name,
                                            raw_url_class_list, i, threads)
            ping_stream.close()
    pool.shutdown()


def ReadPingCSV(stdscr, illlust_name_list: list) -> list:
    illust_class_list = []
    for illust_name in illlust_name_list:
        url_class_list = []
        with open('./PicsDatabase/' + illust_name + '/ping.csv') as ping_stream:
            ping_stream.readline()
            raw_url_list = ping_stream.readlines()
            ping_stream.close
        for raw_url in raw_url_list:
            raw_url_sep = raw_url.rfind(',')
            url = raw_url[:raw_url_sep]
            is_r18 = raw_url[raw_url_sep + 1:len(raw_url) - 1]
            if is_r18 == "False":
                is_r18 = False
            else:
                is_r18 = True
            url_class_list.append(PicClass(is_r18=is_r18,url=url))
        illust_class_list.append(IllustClass(illust_id=0,illust_name=illust_name,pic_class_list=url_class_list))
    return illust_class_list
'''
if f1 == '4' or f1 == '':
if f1 == '5':
'''

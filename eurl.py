import time
from lxml import html
# Debug is available at here
from config import driver_init, stdscr, max_y

stdscr.clear()
stdscr.refresh()
# First config, then uquery
from uquery import illust_id_list, illust_name_list

stdscr.clear()
stdscr.refresh()


class PicClass:
    is_r18: bool
    url: str

    def __init__(self, is_r18, url):
        self.is_r18 = is_r18
        self.url = url


class IllustClass:
    illust_id: str
    illust_name: str
    pic_class_list: list

    def __init__(self, illust_id, illust_name, pic_class_list):
        self.illust_id = illust_id
        self.illust_name = illust_name
        self.pic_class_list = pic_class_list


# isR18:$x("//li[1]//a//div/div/div")
# serial:$x("string(//li[4]//div/span[2])")
# url:...


def web_scroll_3():
    time.sleep(1)
    for i in range(1, 4):
        driver.execute_script(
            '''
                var i = %d * document.body.scrollHeight/3;
                window.scrollTo(0,i);
                ''' % i
        )
        time.sleep(1)


# Examples:

# from:https://i.pximg.net/c/360x360_70/img-master/img/2021/03/13/00/00/06/88401633_p0_square1200.jpg
# to:https://i.pximg.net/img-original/img/2021/03/13/00/00/06/88401633_p0.png

# from:https://i.pximg.net/c/250x250_80_a2/custom-thumb/img/2020/11/07/00/00/12/85503806_p0_custom1200.jpg
# to:https://i.pximg.net/img-original/img/2020/11/07/00/00/12/85503806_p0.jpg
def get_pics_for_each_illust(illust_id):
    # Make len != 0 to enter the loop at least once
    pic_urls_list_on_crawl = [1]
    page_num = 1
    # Get urls page by page, and when the page empty the loop stops
    # Unreliable judgement by page elements down the website
    while len(pic_urls_list_on_crawl) != 0:
        global pic_class_list, stdscr
        url = 'https://www.pixiv.net/users/' + \
              str(illust_id) + '/artworks' + '?p=' + str(page_num)
        stdscr.addstr("Getting url: " + url + '\n')
        stdscr.refresh()
        driver.get(url)
        web_scroll_3()
        time.sleep(3)
        stdscr.addstr("Finished getting url: " + url + '\n')
        stdscr.refresh()
        stdscr.clear()
        page_source = driver.page_source
        page_html = html.etree.HTML(page_source)
        pic_urls_list_on_crawl = page_html.xpath(
            '//img[starts-with(@src,"https://i.pximg.net/c/")]/@src')
        # Change urls & Wrap pic_urls into class
        for i in range(len(pic_urls_list_on_crawl)):
            # Get R-18 tags
            r18_indicator = page_html.xpath(
                "//li[" + str(i + 1) + "]//a//div/div/div")
            if len(r18_indicator) != 0:
                is_r18 = True
            else:
                is_r18 = False
            # Get pic serials
            serial_indicator = page_html.xpath(
                "string(//li[" + str(i + 1) + "]//div/span[2])")
            if len(serial_indicator) != 0:
                serial = int(serial_indicator)
            else:
                serial = 1
            # Change thumbnails into origiinal pics, jpg & png
            if pic_urls_list_on_crawl[i].find("to") != -1:
                url_in_jpg = pic_urls_list_on_crawl[i].replace(
                    "c/250x250_80_a2/custom-thumb", "img-original")
                url_in_jpg = url_in_jpg.replace("_custom1200", '')
            else:
                url_in_jpg = pic_urls_list_on_crawl[i].replace(
                    "c/250x250_80_a2/img-master", "img-original")
                url_in_jpg = url_in_jpg.replace("_square1200", '')
            url_in_png = url_in_jpg.replace("jpg", "png")
            # Start to wrap things together in PicClass
            # Firstly without substitution
            pic_class_in_jpg = PicClass(
                is_r18=is_r18, url=url_in_jpg)
            pic_class_in_png = PicClass(
                is_r18=is_r18, url=url_in_png)
            pic_class_list.append(pic_class_in_jpg)
            pic_class_list.append(pic_class_in_png)
            # Then substitute serials
            for j in range(serial - 1):
                url_in_jpg = url_in_jpg.replace("p" + str(j), "p" + str(j + 1))
                url_in_png = url_in_png.replace("p" + str(j), "p" + str(j + 1))
                pic_class_in_jpg = PicClass(is_r18=
                                            is_r18, url=url_in_jpg)
                pic_class_in_png = PicClass(is_r18=
                                            is_r18, url=url_in_png)
                # Mind the append order
                pic_class_list.append(pic_class_in_jpg)
                pic_class_list.append(pic_class_in_png)
        page_num += 1


# Important global variable
illust_class_list = []
driver = driver_init()
for i in range(len(illust_id_list)):
    pic_class_list = []
    get_pics_for_each_illust(illust_id_list[i])
    # Bound by class
    illust_class_list.append(IllustClass(illust_id_list[i], illust_name_list[i], pic_class_list))
driver.quit()

'''
# Debug output
# For curses cannot row the terminal, it's annoying to get it right.
for i in range(len(illust_class_list)):
    for j in range(len(illust_class_list[i].pic_class_list)):
        url = illust_class_list[i].pic_class_list[j].url
        cur_y = stdscr.getyx()[0]
        if cur_y == max_y:
            stdscr.clear()
            stdscr.refresh()
            stdscr.move(0, 0)
        stdscr.addstr(str(url) + '\n')
        stdscr.refresh()
stdscr.getch()
'''
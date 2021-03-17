from concurrent.futures import ThreadPoolExecutor
from config import driver
from uquery import illusts, illustnames
import time
from lxml import html


class picUrl:
    def __init__(self, isR18, url, illustName):
        self.isR18 = isR18
        self.url = url
        self.illustName = illustName

# isR18:$x("//li[1]//a//div/div/div")
# serial:$x("string(//li[4]//div/span[2])")
# url:...


def WebScroll3():
    for i in range(1, 4):
        driver.execute_script(
            '''
                var i = %d * document.body.scrollHeight/3;
                window.scrollTo(0,i);
                ''' % i
        )
        time.sleep(1)


# from:https://i.pximg.net/c/360x360_70/img-master/img/2021/03/13/00/00/06/88401633_p0_square1200.jpg
# to:https://i.pximg.net/img-original/img/2021/03/13/00/00/06/88401633_p0.png

# from:https://i.pximg.net/c/250x250_80_a2/custom-thumb/img/2020/11/07/00/00/12/85503806_p0_custom1200.jpg
# to:https://i.pximg.net/img-original/img/2020/11/07/00/00/12/85503806_p0.jpg
def getPic(illustID, illustName):
    picUrls = [1]
    pageNum = 1
    while len(picUrls) != 0:
        global picUrlsInList
        url = 'https://www.pixiv.net/users/' + \
            str(illustID) + '/artworks' + '?p=' + str(pageNum)
        driver.get(url)
        WebScroll3()
        time.sleep(3)
        pageSource = driver.page_source
        pageHtml = html.etree.HTML(pageSource)
        picUrls = pageHtml.xpath(
            '//img[starts-with(@src,"https://i.pximg.net/c/")]/@src')

        for i in range(len(picUrls)):

            r18Indicator = pageHtml.xpath(
                "//li[" + str(i + 1) + "]//a//div/div/div")
            if len(r18Indicator) != 0:
                isR18 = True
            else:
                isR18 = False

            serialIndicator = pageHtml.xpath(
                "string(//li[" + str(i + 1) + "]//div/span[2])")
            if len(serialIndicator) != 0:
                serial = int(serialIndicator)
            else:
                serial = 1

            if picUrls[i].find("to") != -1:
                urlInJPG = picUrls[i].replace(
                    "c/250x250_80_a2/custom-thumb", "img-original")
                urlInJPG = urlInJPG.replace("_custom1200", '')
            else:
                urlInJPG = picUrls[i].replace(
                    "c/250x250_80_a2/img-master", "img-original")
                urlInJPG = urlInJPG.replace("_square1200", '')
            urlInPNG = urlInJPG.replace("jpg", "png")

            urlClassInJPG = picUrl(
                isR18=isR18, url=urlInJPG, illustName=illustName)
            urlClassInPNG = picUrl(
                isR18=isR18, url=urlInPNG, illustName=illustName)
            picUrlsInList.append(urlClassInJPG)
            picUrlsInList.append(urlClassInPNG)

            for j in range(serial - 1):
                urlInJPG = urlInJPG.replace("p" + str(j), "p" + str(j + 1))
                urlInPNG = urlInPNG.replace("p" + str(j), "p" + str(j + 1))
                urlClassInJPG = picUrl(
                    isR18=isR18, url=urlInJPG, illustName=illustName)
                urlClassInPNG = picUrl(
                    isR18=isR18, url=urlInPNG, illustName=illustName)
                picUrlsInList.append(urlClassInJPG)
                picUrlsInList.append(urlClassInPNG)
        pageNum += 1


picUrlsInList = []
for i in range(len(illusts)):
    getPic(illusts[i], illustnames[i])
for i in range(len(picUrlsInList)):
    print(picUrlsInList[i].url)

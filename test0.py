from selenium import webdriver
import os
import time
from lxml import html
from fake_useragent import UserAgent
import requests
from multiprocessing import Process, Pool, Manager
import queue
ua = UserAgent()
etree = html.etree
profile_dir = r'C:\\Users\\chen\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\twtf6r6t.default-release'
profile = webdriver.FirefoxProfile(profile_dir)
driver = webdriver.Firefox(profile)


class ImgUrl:
    def __init__(self, url, h_flag, serial):
        self.url = url
        self.h_flag = h_flag
        self.serial = serial


def WebScroll3():
    for i in range(1, 4):
        driver.execute_script(
            '''
                var i = %d * document.body.scrollHeight/3;
                window.scrollTo(0,i);
                ''' % i
        )
        time.sleep(1)


def GetUrl(illustID, illustName, page_num, q):
    global driver
    url = 'https://www.pixiv.net/users/' + \
        str(illustID) + '/artworks' + '?p=' + str(page_num)
    driver.get(url)  # Default debug dial: 544479
    WebScroll3()
    time.sleep(5)
    page = driver.page_source
    dom = etree.HTML(page)
    ids = dom.xpath(
        '//img[starts-with(@src,"https://i.pximg.net/c/")]/@src')
    illustName = illustName.replace('/', '-')
    if os.path.exists('./LSP/' + illustName + '/') == False:
        os.mkdir('./LSP/' + illustName + '/')
    if os.path.exists('./LSP/' + illustName + '/' + illustName + '-NR/') == False:
        os.mkdir('./LSP/' + illustName + '/' + illustName + '-NR/')
    for p in range(len(ids)):
        if ids[p].find('custom-thumb') != -1:
            ids[p] = ids[p].replace('https://i.pximg.net/c/250x250_80_a2/custom-thumb/',
                                    'https://i.pximg.net/img-original/')
            ids[p] = ids[p].replace('_custom1200.jpg', '.jpg')
        elif ids[p].find('img-master') != -1:
            ids[p] = ids[p].replace('https://i.pximg.net/c/250x250_80_a2/img-master/',
                                    'https://i.pximg.net/img-original/')
            ids[p] = ids[p].replace('_square1200.jpg', '.jpg')
        ImgUrl.url = ids[p]
        h_flag = False
        h_id = dom.xpath(
            'string(/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div/section/div[3]/div/ul/li['+str(p + 1)+']/div/div[1]/div/a/div[1]/div[1]/div/div)')
        if len(h_id) != 0:
            h_flag = True
        pic_num = 1
        if len(dom.xpath('//li[' + str(p + 1) + ']/div/div[1]/div/a/div[1]/div[2]/div/span[2]')) != 0:
            # 有图组 If there's a series
            pic_num = dom.xpath(
                'number(//li[' + str(p + 1) + ']/div/div[1]/div/a/div[1]/div[2]/div/span[2])')
        q.put(ImgUrl(ids[p], h_flag, pic_num))
    print('page %d is in.' % page_num)

# 图片链接记得改。组图全是同一张！


def GetPic(illustName, newID_group, start, end):
    for i in range(start, end):
        picID = ''
        for char in newID_group[i].url[-15:-7]:
            picID += char
        headers = {'User-Agent': ua.random,
                   'Referer': 'https://www.pixiv.net/artworks/' + picID}
        sleep_time = 4
        if newID_group[i].h_flag:
            if os.path.exists('./LSP/' + illustName + '/' + illustName + '-R/') == False:
                os.mkdir('./LSP/' + illustName + '/' + illustName + '-R/')
        for j in range(int(newID_group[i].serial)):
            r = requests.get(newID_group[i].url, headers=headers)
            newID_group[i].url = newID_group[i].url.replace(
                '_p'+str(j), '_p' + str(j + 1))
            file_name = picID + '-' + str(j)
            if r.status_code == 200:
                if newID_group[i].h_flag:
                    with open('./LSP/' + illustName + '/' + illustName + '-R/' + file_name + '.jpg', 'wb') as f:
                        f.write(r.content)
                    time.sleep(sleep_time)
                else:
                    with open('./LSP/' + illustName + '/' + illustName + '-NR/' + file_name + '.jpg', 'wb') as f:
                        f.write(r.content)
                    time.sleep(sleep_time)
            else:
                newID_group[i].url = newID_group[i].url.replace('.jpg', '.png')
                r = requests.get(newID_group[i].url, headers=headers)
                if r.status_code == 200:
                    if newID_group[i].h_flag:
                        with open('./LSP/' + illustName + '/' + illustName + '-R/' + file_name + '.png', 'wb') as f:
                            f.write(r.content)
                        time.sleep(sleep_time)
                    else:
                        with open('./LSP/' + illustName + '/' + illustName + '-NR/' + file_name + '.png', 'wb') as f:
                            f.write(r.content)
                        time.sleep(sleep_time)
                else:
                    print('Er.')
            time.sleep(3)


if __name__ == '__main__':
    if os.path.exists('./LSP/') == False:
        os.mkdir('./LSP/')
    driver.get('https://www.pixiv.net/setting_user.php')
    inital_page = driver.page_source
    initial_dom = etree.HTML(inital_page)
    r18Switch = initial_dom.xpath(
        '//input[(@name="r18" or @name="r18g") and @checked]/@value')
    if r18Switch[0] == 'hide':
        print('R-18 disabled.')
    else:
        print('R-18 enabled.')
    if r18Switch[1] == '1':
        print('R-18G disabled.')
    else:
        print('R-18G enabled.')
    conf = input(
        'Do you want confirm the r-18 settings?\nPress Y or Enter to navigate you to the settings page, or by default NO.\n')
    flag = False
    if conf == 'y' or conf == 'Y' or conf == '':
        flag = True
    if flag:
        driver.get('https://www.pixiv.net/setting_user.php')
        r18Config = input('Unleash R-18?\n')
        r18gConfig = input('Unleash R-18G?\n')
        if r18Config == 'y' or r18Config == 'Y' or r18Config == '':
            driver.find_element_by_xpath(
                '//input[@name="r18" and @value="show"]').click()
            print('R-18 has been ON.')
        else:
            driver.find_element_by_xpath(
                '//input[@name="r18" and @value="hide"]').click()
            print('R-18 is now OFF.')
        if r18gConfig == 'Y' or r18Config == 'y' or r18gConfig == '':
            driver.find_element_by_xpath(
                '//input[@name="r18g" and @value="2"]').click()
            print('R-18G has been ON.')
        else:
            driver.find_element_by_xpath(
                '//input[@name="r18g" and @value="1"]').click()
            print('R-18G is now OFF.')
        driver.find_element_by_xpath('//input[@name="submit"]').click()
        time.sleep(2)
        print('Config saved. Now refreshing...')
        driver.refresh()
    flag = True
    while flag:
        illustID = input(
            'Which illustrator do you want to query into?\nPlease input his/her ID:')
        initial_url = 'https://www.pixiv.net/users/' + \
            str(illustID) + '/artworks' + '?p=1'
        original_r = requests.get(initial_url)
        if original_r.status_code != 200:
            print('No illustrator found!')
        else:
            driver.get(initial_url)
            inital_page = driver.page_source
            initial_dom = etree.HTML(inital_page)
            illustName = initial_dom.xpath('string(//h1)')
            page_total = 1
            while len(initial_dom.xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/div[3]/a[' + str(page_total) + ']')) != 0:
                page_total += 1
            page_total -= 2
            conf = input('Confirmation: Is this guy the one you want?' + '\n' +
                         illustName + '\n' + 'Press Y or Enter to confirm, otherwise NO by default!\n')
            if conf == 'y' or conf == 'Y' or conf == '':
                flag = False
            else:
                print('Now you may type again.')
    driver.close()
    page_num = page_total
    print('Now navigating you to the illustrator_s homepage...')
    pool = Pool(processes=4)
    q = Manager().Queue()
    print('Now the carnival begins!')
    ids = []
    for i in range(1, page_total):
        pool.apply_async(GetUrl, (illustID, illustName, i, q,))
        time.sleep(1)
        while True:
            try:
                item = q.get(block=False)
                ids.append(item)
            except(queue.Empty):
                break
    pool.apply(GetUrl, (illustID, illustName, page_total, q))
    while True:
        try:
            item = q.get(block=False)
            ids.append(item)
        except(queue.Empty):
            break
    # print(len(ids))
    id_len = len(ids)
    num = []
    delta = int(id_len / 4)
    tail = id_len % 4
    for i in range(4):
        num.append(delta)
    for i in range(tail):
        num[i] += 1
    n = []
    n.append(0)
    n.append(num[0] + 1)
    for i in range(2, 5):
        n.append(n[i - 1] + num[i - 1])
    for i in range(3):
        pool.apply_async(GetPic, (illustName, ids, n[i], n[i + 1]))
        time.sleep(1)
    pool.apply(GetPic, (illustName, ids, n[3], n[4]))
    pool.close()
    pool.join()
    # pool.terminate()

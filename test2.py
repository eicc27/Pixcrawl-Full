from selenium import webdriver
import os
import time
from lxml import html
from fake_useragent import UserAgent
import requests
# 尝试获取图集的信息（完成！）
# Try to identify a SERIES of pics. (Completed!)
# 尝试切换页面（完成！）、自定义页面（完成！）
# Try to trun the pages and manually select the illustrator. (Completed!)
# 尝试R-18开关（开关完成;程序读写完成）（分开来放置-illustID + R文件夹和NR文件夹：完成）
# Try to manually configure the R-18 & R-18G switch. (Completed!)
# Try to seperate the restricted and non-restricted pics using different folders. (Completed!)
# 遇到同名的，直接跳过，不要sleep！（完成！）
# When encountering a same pic, skip it directly without waiting. (Completed!)
# 程序的底层设计：牺牲时间复杂度换取准确度。如果网络环境不大好，那么复杂度会根据需求进一步提高！
# The basic design is to sacrifice speed for accuracy. It may require more sleeping when connection is bad.
# bug:可能要先点击“浏览全部”展开，再点击图片。(已解决)
# pngs require clicking the original pictures(zoom). (Completed!)
# another element <button class="emr523-0 cwSjFV" type="button"> obscures it
# 待解决：画师更新图片之后，不能用这种方法解决。可以考虑从最后一页开始读取图片，避免麻烦。
# Improvements to be done: illustrator's update (half-done, prepared for plug-in)
# todo: optimize variables naming


def WebScroll3():
    driver.execute_script(
        '''
        var i = document.body.scrollHeight/3;
        window.scrollTo(0,i);
        '''
    )
    time.sleep(1)
    driver.execute_script(
        '''
        var i = 2 * document.body.scrollHeight/3;
        window.scrollTo(0,i);
        '''
    )
    time.sleep(1)
    driver.execute_script(
        '''
        var i = document.body.scrollHeight;
        window.scrollTo(0,i);
        '''
    )
    time.sleep(3)


ua = UserAgent()
etree = html.etree
profile_dir = r'C:\\Users\\chen\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\twtf6r6t.default-release'
profile = webdriver.FirefoxProfile(profile_dir)
driver = webdriver.Firefox(profile)
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
            print('Now navigating to configuration...')
            flag = False
        else:
            print('Now you may type again.')
page_num = page_total
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
conf = input('Do you want confirm the r-18 settings?\nPress Y or Enter to navigate you to the settings page, or by default NO.\n')
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
print('Now navigating you to the illustrator_s homepage...')
i = 0  # 正常的图片，在文件夹里的编号 Normal pics' numbering in the NR-folder
hi = 0  # R图片，在文件夹里的编号 Restricted pics' numbering in the R-folder
i_total = 0  # 所有的编号 All pic's numbering
while page_num > 0:  # 同一个画师 Loops with a same illstrator
    url = 'https://www.pixiv.net/users/' + \
        str(illustID) + '/artworks' + '?p=' + str(page_num)
    driver.get(url)  # Default debug dial: 544479
    WebScroll3()
    page = driver.page_source
    dom = etree.HTML(page)
    ids = dom.xpath(
        '//img[starts-with(@src,"https://i.pximg.net/c/")]/@src')
    illustName = illustName.replace('/', '-')
    if os.path.exists('./LSP/' + illustName + '/') == False:
        os.mkdir('./LSP/' + illustName + '/')
    if os.path.exists('./LSP/' + illustName + '/' + illustName + '-NR/') == False:
        os.mkdir('./LSP/' + illustName + '/' + illustName + '-NR/')
    for p in range(len(ids) - 1, -1, -1):  # 倒着来遍历 Reversed
        # print(id)
        i_total += 1  # 暂时仅用于文件命名 Temp. only used to name files
        h_id = dom.xpath(
            'string(/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div/section/div[3]/div/ul/li['+str(p + 1)+']/div/div[1]/div/a/div[1]/div[1]/div/div)')
        if len(h_id) == 0:
            i += 1
        else:
            hi += 1
            if os.path.exists('./LSP/' + illustName + '/' + illustName + '-R/') == False:
                os.mkdir('./LSP/' + illustName + '/' + illustName + '-R/')
        if ids[p].find('custom-thumb') != -1:
            newID = ids[p].replace('https://i.pximg.net/c/250x250_80_a2/custom-thumb/',
                                   'https://i.pximg.net/img-original/')
            newID = newID.replace('_custom1200.jpg', '.jpg')
        elif ids[p].find('img-master') != -1:
            newID = ids[p].replace('https://i.pximg.net/c/250x250_80_a2/img-master/',
                                   'https://i.pximg.net/img-original/')
            newID = newID.replace('_square1200.jpg', '.jpg')
            newID_alt = newID.replace('.jpg', '.png')
        picID = ''
        for char in newID[-15:-7]:
            picID += char
        j = 1
        k = 0
        if len(dom.xpath('//li[' + str(p + 1) + ']/div/div[1]/div/a/div[1]/div[2]/div/span[2]')) != 0:
            # 有图组 If there's a series
            j = dom.xpath(
                'number(//li[' + str(p + 1) + ']/div/div[1]/div/a/div[1]/div[2]/div/span[2])')
        if len(h_id) == 0:
            while k < j:  # 同一组NR图 A same series of NR pics
                # print(newID)
                flag = True
                file_name = str(illustID) + '-' + str(i) + '-NR' + '_' + str(k)
                if os.path.exists('./LSP/' + illustName + '/' + illustName + '-NR/' + file_name + '.png') == True or os.path.exists('./LSP/' + illustName + '/' + illustName + '-NR/' + file_name + '.jpg') == True:
                    # 如果存在这个文件 If the file already exists
                    print(file_name + ' seems to have been in existence.')
                    flag = False
                if flag:
                    headers = {'User-Agent': ua.random,
                               'Referer': 'https://www.pixiv.net/artworks/' + picID}
                    r = requests.get(newID, headers=headers)
                    newID_alt = newID.replace('.jpg', '.png')
                    if r.status_code == 200:  # 如果jpg行得通 If '.jpg' works
                        with open('./LSP/' + illustName + '/' + illustName + '-NR/' + file_name + '.jpg', 'wb') as f:
                            f.write(r.content)
                        time.sleep(1.5)
                    else:  # 如果jpg行不通，那就试试png Then try '.png'
                        driver.get('https://www.pixiv.net/artworks/' + picID)
                        # 等待页面加载————必须点开大图才能进一步操作，否则即使有了referer还是403... Waiting for webpage loading
                        if len(driver.find_elements_by_xpath('//div[2]/button/div[2]')) != 0:
                            driver.find_element_by_xpath(
                                '//div[2]/button/div[2]').click()
                        # 点击“展开”按钮 Show all pics(The button is obscuring the pic)
                        time.sleep(2)
                        driver.find_element_by_xpath('//div[2]/a/img').click()
                        time.sleep(1)
                        # 点开大图 Click on the pic
                        r = requests.get(newID_alt, headers=headers)
                        if r.status_code == 200:
                            with open('./LSP/' + illustName + '/' + illustName + '-NR/' + file_name + '.png', 'wb') as f:
                                f.write(r.content)
                            time.sleep(2)
                newID = newID.replace(str(k) + '.jpg', str(k + 1) + '.jpg')
                newID_alt = newID.replace('.jpg', '.png')
                k += 1
        else:
            while k < j:  # 同一组R图 A same series of restricted pics
                # print(newID)
                flag = True
                file_name = str(illustID) + \
                    '-' + str(hi) + '-R' + '_' + str(k)
                if os.path.exists('./LSP/' + illustName + '/' + illustName + '-R/' + file_name + '.png') == True or os.path.exists('./LSP/' + illustName + '/' + illustName + '-R/' + file_name + '.jpg') == True:
                    print(file_name + ' seems to have been in existence.')
                    flag = False
                if flag:
                    headers = {'User-Agent': ua.random,
                               'Referer': 'https://www.pixiv.net/artworks/' + picID}
                    r = requests.get(newID, headers=headers)
                    newID_alt = newID.replace('.jpg', '.png')
                    if r.status_code == 200:  # 如果jpg行得通
                        with open('./LSP/' + illustName + '/' + illustName + '-R/' + file_name + '.jpg', 'wb') as f:
                            f.write(r.content)
                        time.sleep(1.5)
                    else:  # 如果jpg行不通，那就试试png
                        if len(driver.find_elements_by_xpath('//div[2]/button/div[2]')) != 0:
                            driver.find_element_by_xpath(
                                '//div[2]/button/div[2]').click()
                            time.sleep(1)
                        driver.get('https://www.pixiv.net/artworks/' + picID)
                        # 等待页面加载————必须点开大图才能进一步操作，否则即使有了referer还是403...
                        time.sleep(2)
                        driver.find_element_by_xpath('//div[2]/a/img').click()
                        # 等待request发送 Waiting for request sending
                        time.sleep(1)
                        r = requests.get(newID_alt, headers=headers)
                        if r.status_code == 200:
                            with open('./LSP/' + illustName + '/' + illustName + '-R/' + file_name + '.png', 'wb') as f:
                                f.write(r.content)
                            time.sleep(2)
                newID = newID.replace(str(k) + '.jpg', str(k + 1) + '.jpg')
                newID_alt = newID.replace('.jpg', '.png')
                k += 1
        time.sleep(2)
    time.sleep(5)
    print('Page ' + str(page_num) + ' has completed.')
    page_num -= 1
print('All completed.')

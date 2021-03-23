from msedge.selenium_tools import Edge, EdgeOptions
from lxml import html
import time

f0 = input("Config R18?\nWarning: you must quit all edge browsers and kill their process in task manager!")
options = EdgeOptions()
options.use_chromium = True
profileDir = r"--user-data-dir=C:\Users\Chan\AppData\Local\Microsoft\Edge\User Data"
options.add_argument(profileDir)
driver = Edge(options=options)
if f0 == 'Y' or f0 == 'y' or f0 == '':
    driver.get("https://www.pixiv.net/setting_user.php")
    etree = html.etree
    initial_page = driver.page_source
    initial_dom = etree.HTML(initial_page)
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
    if conf == 'y' or conf == 'Y' or conf == '':
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

         
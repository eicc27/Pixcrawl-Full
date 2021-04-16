from msedge.selenium_tools import Edge, EdgeOptions
from lxml import html
import time
import curses
stdscr = curses.initscr()
max_y = stdscr.getmaxyx()[0] - 1
if max_y < 16:
    raise Exception("Terminal row size must be more then 17, but now it is %d." % (max_y + 1))
# changelog: more OOP.
# class: illust,illustName,picList(made up of pic classes)


def driver_init():
    options = EdgeOptions()
    options.use_chromium = True
    profile_dir = r"--user-data-dir=C:\Users\Chan\AppData\Local\Microsoft\Edge\User Data"
    options.add_argument(profile_dir)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = Edge(options=options)
    return driver


stdscr.addstr("Config R18?\nWarning: you must quit all edge browsers and kill their process in task manager!")
# When getstr(), auto-refresh
f0_config = bytes.decode(stdscr.getstr())
if f0_config == 'Y' or f0_config == 'y' or f0_config == '':
    driver = driver_init()
    driver.get("https://www.pixiv.net/setting_user.php")
    etree = html.etree
    initial_page = driver.page_source
    initial_dom = etree.HTML(initial_page)
    r18Switch = initial_dom.xpath(
        '//input[(@name="r18" or @name="r18g") and @checked]/@value')
    if r18Switch[0] == 'hide':
        stdscr.addstr('R-18 disabled.\n')
    else:
        stdscr.addstr('R-18 enabled.\n')
    if r18Switch[1] == '1':
        stdscr.addstr('R-18G disabled.\n')
    else:
        stdscr.addstr('R-18G enabled.\n')
    stdscr.refresh()

    stdscr.addstr(
        'Do you want confirm the r-18 settings?\nPress Y or Enter to navigate you to the settings page, or by default '
        'NO.\n')
    f1_config = bytes.decode(stdscr.getstr())
    if f1_config == 'y' or f1_config == 'Y' or f1_config == '':
        stdscr.addstr('Unleash R-18?\n')
        r18Config = bytes.decode(stdscr.getstr())
        stdscr.addstr('Unleash R-18G?\n')
        r18gConfig = bytes.decode(stdscr.getstr())
        if r18Config == 'y' or r18Config == 'Y' or r18Config == '':
            driver.find_element_by_xpath(
                '//input[@name="r18" and @value="show"]').click()
            stdscr.addstr('R-18 has been ON.\n')
        else:
            driver.find_element_by_xpath(
                '//input[@name="r18" and @value="hide"]').click()
            stdscr.addstr('R-18 is now OFF.\n')
        # Give a timely feedback
        stdscr.refresh()
        if r18gConfig == 'Y' or r18gConfig == 'y' or r18gConfig == '':
            driver.find_element_by_xpath(
                '//input[@name="r18g" and @value="2"]').click()
            stdscr.addstr('R-18G has been ON.\n')
        else:
            driver.find_element_by_xpath(
                '//input[@name="r18g" and @value="1"]').click()
            stdscr.addstr('R-18G is now OFF.\n')
        stdscr.refresh()
        driver.find_element_by_xpath('//input[@name="submit"]').click()
        time.sleep(2)
        stdscr.addstr('Config saved. Now refreshing...\n')
        stdscr.refresh()
        driver.refresh()
    driver.quit()

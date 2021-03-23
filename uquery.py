from urllib import request as req
from urllib import error
from fake_useragent import UserAgent
import re


def installopener():
    headers = [('User-Agent', UserAgent().random),
               ('Referer', 'https://www.pixiv.net')]
    opener = req.build_opener()
    opener.addheaders = headers
    req.install_opener(opener)


def getIllust(illust):
    openUrl = req.urlopen(
        "https://www.pixiv.net/users/" + illust + "/artworks?p=1")
    if openUrl.getcode() != 200:
        print("Error! Please retype.")
        raise error.HTTPError
    openUrlBytes = openUrl.read()
    titleInBytes = re.findall(b'<title>(.+)</title>', openUrlBytes)
    illustName = titleInBytes[0].decode('utf-8').rstrip("のイラスト・マンガ - pixiv")
    print(illustName)
    illustName = illustName.replace('/', '')
    illustnames.append(illustName)


isLoop = 1
while isLoop:
    illustInput = input(
        "Which illustrator do you want to query into?\nPlease input his/her ID(using ',' to divide):\nWarning: Do not forget to open your VPN!")
    illusts = []
    illustInput = illustInput.rstrip(',')
    illustInput = illustInput.replace(' ','')
    while(illustInput.find(',') != -1):
        pos = illustInput.find(',')
        illusts.append(illustInput[0:pos])
        stripStr = illustInput[0:pos+1]
        illustInput = illustInput[len(stripStr):]
    illusts.append(illustInput)
    installopener()
    illustnames = []
    try:
        for illust in illusts:
            getIllust(illust)
    except error.HTTPError:
        print("Error happens, please retype.")
    confKey = input('Confirm: this(these)?')
    if(confKey == 'Y' or confKey == 'y' or confKey == ''):
        isLoop = 0
    else:
        print("You may type again.")
print(illustnames)

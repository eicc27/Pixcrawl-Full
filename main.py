import time
from urllib import request as req
from urllib import error as err
import os
from concurrent.futures import ThreadPoolExecutor
import config
import uquery
import gurl as g
from fake_useragent import UserAgent


def downloadurl(picUrlInClass):
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
        rdownload = req.urlopen(picUrlInClass.url)
        print("Starting downloading of: " + downloadName)
        with open(picPath, "wb") as filewrite:
            filewrite.write(rdownload.read())
        print("Completed downloading of: " + downloadName)
    except err.HTTPError:
        pass


if __name__ == '__main__':
    if not os.path.exists("./LSP"):
        os.mkdir("./LSP")
    urls = g.picUrlsInList
    print(len(urls), "pics are in.")
    pool = ThreadPoolExecutor(max_workers=16)
    for i in range(len(urls)):
        print("target:", urls[i].url)
        pool.submit(downloadurl, urls[i])
    pool.shutdown()
    print("DOWNLOAD COMPLETE. PLEASE QUIT MANUALLY.")

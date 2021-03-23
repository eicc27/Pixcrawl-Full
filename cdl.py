class picUrl:
    def __init__(self, isR18, url, illustName):
        self.isR18 = isR18
        self.url = url
        self.illustName = illustName


with open("./pics.csv", "r") as pics:
    ostr = pics.readlines()
pics.close()

ourls = []

for urlClass in ostr:
    urlClass = urlClass.rstrip('\n')
    c0 = urlClass.find(',')
    isR18 = urlClass[:c0]
    urlClass = urlClass[c0 + 1:]
    c1 = urlClass.find(',')
    url = urlClass[:c1]
    urlClass = urlClass[c1 + 1:]
    illustName = urlClass
    ourls.append(picUrl(isR18=isR18,url=url,illustName=illustName))



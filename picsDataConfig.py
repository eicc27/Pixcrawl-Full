#Get a special folder full of CSV files, named with illusts' names.
#Structure:
#./PicsDatabase/${illustName}/${raw},${download}
#${raw}: Crawled links with both .jpg & .png ext.
#${download}: When testing, urls returning 404 will be excluded from ${Raw}
#FIRST LINE: ${illustName},${illustID},${indexNum},${scanTimes}
'''
illustName: name
illustID: id
indexNum: number of pics
scanTimes: times querying the illust
'''
#rest lines: same as pics.csv

f1str0 = "Database mode has 6 options, which all queries illusts.csv:\n"
f1str1 = "[1]. <Webdriver imported> Crawl pics only\n"
f1str2 = "[2]. <raw.csv needed> Query crawled pics only\n"
f1str3 = "[3]. <ping.csv needed> Download crawled pics only\n"
f1str4 = "[4](default). Crawl pics ----> Query pics\n"
f1str5 = "[5]. <raw.csv needed> Query pics ----> Download from ping.csv\n"
f1str6 = "[6]. Crawl pics ----> Query pics ----> Download from ping.csv\n"
f1str = f1str0 + f1str1 + f1str2 + f1str3 + f1str4 + f1str5 + f1str6
f1_picsdata = input(f1str)

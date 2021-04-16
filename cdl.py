class PicClass:
    def __init__(self, is_r18, url):
        self.is_r18 = is_r18
        self.url = url


class IllustClass:
    def __init__(self, illust_code, illust_name, pic_class_list):
        self.illust_code = illust_code
        self.illust_name = illust_name
        self.pic_class_list = pic_class_list


with open("./pics.csv", "r", encoding="utf-8") as pics:
    ostr = pics.readlines()
pics.close()

# This can be realized thanks to csv file
illust_class_list = []
pic_class_list = []
for i in range(len(ostr)):
    this_illust_name = ostr[i][ostr[i].rfind(',') + 1: len(ostr[i]) - 1]
    this_is_r18 = ostr[i][:ostr[i].find(',')]
    this_url = ostr[i].rstrip(',' + this_illust_name + '\n').lstrip(this_is_r18 + ',')
    prev_illust_name = ostr[i - 1][ostr[i - 1].rfind(',') + 1: len(ostr[i - 1]) - 1]
    if prev_illust_name == this_illust_name:
        pic_class_list.append(PicClass(this_is_r18, this_url))
    else:
        illust_class_list.append(IllustClass(
            0, prev_illust_name, pic_class_list))
        pic_class_list = []
    if i == len(ostr) - 1:
        if this_illust_name != prev_illust_name:
            illust_class_list.append(IllustClass(
                0, this_illust_name, PicClass(this_is_r18, this_url)))
        elif len(illust_class_list) == 0:
            illust_class_list.append(IllustClass(
                0, this_illust_name, pic_class_list))

# ***使用说明***

# 关于此程序的一些重要提示：
# 1. 这个单线程版本之所以会保留，只是因为留作纪念用。我不期望它能十分正常地跑起来。
# 2. 过了两三个月后，requests.get()方法对于我的VPN不再适用。一旦get了pixiv的官网，就会无限卡死。debug不能起任何作用。
# 3. 原来的多进程版本，在参考多方建议下，改成了进程池。其中有效的，有gui和non-gui版本，参考不同的branch。
# 4. 工具狐似乎在selenium的操纵下会抽风。会报一些奇怪的错误（然而，极为偶尔地，还是能够跑起来）。

## 关于程序适用性问题和码风问题

1. 本程序仅能保证在本人的相关配置环境、网络环境下正常运行。

    `Firefox 83.0, automated with Selenium 3.141.0`

    关于网络环境问题：墙内，一定需求VPN。

2. 对于程序中的下段代码：

    ```apache
    profile_dir = r'C:\\Users\\chen\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\twtf6r6t.default-release'
    profile = webdriver.FirefoxProfile(profile_dir)
    driver = webdriver.Firefox(profile)
    ```

    * 更改首行的文件路径为您自己的浏览器用户数据文件夹。
    * 如果您使用的不是*工具狐83.0*或*近期/更新*版本，请使用搜索引擎搜索应该如何初始化，关键字为：

    `Selenium Chrome(或者 IE/Firefox 早期版本/Opera...)`

    语法大同而小异。但是，照搬我的工具狐的代码会有问题！
    
    对于多进程最后的下载图片函数，我换成了多线程池。这对于I/O密集型处理比较有帮助。之前做的进程池，损耗有点大。

3. 由于我是零基础学起（别说程序里的js和xpath了，甚至包括python），程序写就比较仓促，仅仅做了功能性优化，顺便优化了代码结构（没错，原来的代码更加凌乱），我已经在开头和关键位置尽量注释了一些提示。如果是想爬虫入门，我还是建议爬更容易爬到的网站，并且参考代码风格比较简洁的up主/csdn程序员的实例代码，而不是我的。

## 程序本身的一些说明

1. 您必须事先新建一个名字为“LSP”的文件夹，在此程序所在的根目录下。

2. 所有的一级文件夹以画师名字命名，二级文件夹分成R和NR。图片从最后一页开始爬取，同一图集的图片以“_serial”的形式命名。

3. （*已被证实不实，加了Referer和UA之后一切正常*）png类型图片经过实测，加了referer之后似乎还是有问题。因此，直接selenium把它点成大图。这里，需要打开新网页，并且操作不能太快，因此，png文件从程序设计本身比jpg文件慢得多。（可以试试rurudo（25760573）和宮瀬まひろ（5444479））

4. 如果您的网络不好，可以适当地调高一些地方的`time.sleep(secs)`中的`secs`值。这是因为，被selenium操纵的工具狐似乎不会等到网页完全读取完成就进行后续操作/关闭标签页。当然，如果浏览器是Chrome或者是Edge等之类，可能没有这个问题。

5. 检查程序是否正常工作（debug）的基本方法：

    * 看图片编号是否连续。
    * 抽检，看是否有R和NR混在一起的情况。
    * 对于程序本身，建议打断点。

6. 本程序不保证及时更新。由于pixiv似乎会切换固定的网址表示形式，程序需要及时更改其中的一些链接字符串才能正常工作。不过至少目前，它行。

# ***Program Instructions***


# Important annotations:
# 1. The only role the program plays is a memorial.
# 2. The requests.get() method is no longer viable for 'http://www.pixiv.net', cause it jams, and I couldn't know where went wrong.
# 3. Firefox driver automation is given up because some extremely wierd problems happen. (Failed to decode..., and other problems. However it runs occasionally.)
# 4. Currently available version is thread pool version, categorized as gui and non-gui. Compared with multiprocessing (which is good at CPU-dense task), multithreading is better at dealing with I/O problems.

## About compatibility and coding style

1. The program can only be guaranteed to perform normally in my OWN coding, parsing, and network environment.

    `Firefox 83.0, automated with Selenium 3.141.0`

2. For the following codes:

     ```apache
    profile_dir = r'C:\\Users\\chen\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\twtf6r6t.default-release'
    profile = webdriver.FirefoxProfile(profile_dir)
    driver = webdriver.Firefox(profile)
    ```

    * You should modify the path to your own browser's cache path.
    * Note that there are small but fatal difference between browsers'(e.g., IE, Chrome, Edge, Opera...) initialization with Selenium. You may search the method on the Internet.

    * At the last part of the program, I finally chose ALLOCATIVE(allocate a certain length of urls for the function to operate) not DISTRIBUTIVE(give processes a single url at a time). If a higher accuracy is needed, consider using distributive method instead.

3. Because of hurriedness, the coding style is not very uniform and sometimes might cause confusion. At the beginning and some vital points, I've tried my best to add some annotations to make things clear. Anyway, I would never spare my apologies for any problems caused.

## Instuctions of the program itself

1. A new folder named "LSP" must be firstly present in the program's current folder.

2. All primary folder is named after illustrators, and all secondary ones are seperated with "Restricted"(R) and "Not-Restricted"(NR), and the pictures are crawled from the last page, with the same series identified with "_serial" ending.

3. (Proved fake, with UA and Referer given, nothing wrong happens after the test)In the field test, .png file urls seems to sometimes deny my request(403) even with the illustrator's homepage referrer. So I have to use Selenium to click it open, which involves waiting the webpage open and clicking to zoom the picture. This is why, from the perspective of the program design, crawling down pngs is much slower than jpgs. (Take rurudo(25760573) and 宮瀬まひろ(5444479) for example!)

4. If your connection is bad, you may moderately increase the time the progrm sleeps by adjusting the number in the brackets of `time.sleep()`.

5. Some basic methods to test whether the program is running well:

    * Check if the serial numbers of the pics are consecutive.
    * Arbitrarily check if R and NR pics have been misplaced.
    * Use breakpoints.

6. The program is not necessarily up to date. Because pixiv sometimes changes its url format, at that time the strings in the program must be simultaneously updated.

# Important:
   This program has some issues rendering the downlading process and has to be revised. A non-cursor package-like program is under development.
   
   The program here is to be archived so as to represent a footprint of my way of Python.
   
   Next time, a more powerful command-line version including a command-line parsing library(CLI), a more strategic multiprocessing distribution, and a colored font library would be released as a new repo.
   
# ***使用说明***

# 此程序使用curses库来绘制下载GUI。请保证以标准终端运行（而不是Pycharm的控制台），并确保不要随意改变终端窗口的大小。
# 此程序另使用一个.csv文件来实现“即使强行终止/下载失败后仍能接续”的功能。

## 关于程序适用性问题和码风问题

1. 本程序仅能保证在本人的相关配置环境、网络环境下正常运行。

    `Python 3.9, with Windows terminal`

    `Microsoft Edge 89.0.774.57, automated with msedge_selenium_tools 3.141.3`

    关于网络环境问题：墙内，一定需求VPN。

2. 对于程序中的下段代码：

    ```apache
    profileDir = r"--user-data-dir=C:\Users\Chan\AppData\Local\Microsoft\Edge\User Data"
    ```

    * 更改文件路径为您自己的浏览器用户数据文件夹。
    * 如果您使用的不是*Edge 89*或*近期/更新*版本，请使用搜索引擎搜索应该如何初始化，关键字为：

    `Selenium Chrome(或者 IE/Firefox/Opera...)`

    语法大同而小异。但是，照搬我的代码会有问题！
    
    对于多线程，直接使用`concurrent.futues`中的`ThreadPoolExecutor`， 方便省事还高效精准。

3. 由于我是零基础学起（别说程序里的js和xpath了，甚至包括python），程序写就比较仓促，仅仅做了功能性优化，顺便优化了代码结构（没错，原来的代码更加凌乱），我已经在一些关键的代码块前后加上空行作为提示。如果是想爬虫入门，我还是建议爬更容易爬到的网站，并且参考代码风格比较简洁的up主/csdn程序员的实例代码，而不是我的。

## 程序本身的一些说明

1. 您必须事先新建一个名字为“LSP”的文件夹，在此程序所在的根目录下。

2. 所有的一级文件夹以画师名字命名，二级文件夹分成R和NR。图片从第一页开始爬取，同一图集的图片以“_serial”的形式命名。

3. 如果您的网络不好，可以适当地调高一些地方的`time.sleep(secs)`中的`secs`值。

4. 打开网页、获取画师名字的时候并不是多线程。因此可能会稍微有些慢。至于为什么不用，获取画师名字是因为要与我们输入的先后顺序对应，告诉程序“这串数字对应这个画师”；打开网页只是考虑到因为网络环境和内存可能不允许打开多个网页的可能，我还是希望我的程序少占点内存。

5. 检查程序是否正常工作（debug）的基本方法：

    * 将多线程改成单线程，直接传函数。
    * 抽检，看是否有R和NR混在一起的情况。
    * 对于程序本身，建议打断点。

6. 本程序不保证及时更新。由于pixiv似乎会切换固定的网址表示形式，程序需要及时更改其中的一些链接字符串才能正常工作。不过至少目前，它行。

# ***Program Instructions***

# The program uses curses to draw GUI on TERMINAL. Make sure your terminal is not a console that is used to simulate the terminal. Moreover, DO NOT change the terminal's size during the downloading process.
# The program creates a .csv file to enable continual downloading. So even after the program is mandatorily stopped or downloading error happens, it can continue.

## About compatibility and coding style

1. The program can only be guaranteed to perform normally in my OWN coding, parsing, and network environment.

    `Python 3.9, with Windows terminal`

    `Microsoft Edge 89.0.774.57, automated with msedge_selenium_tools 3.141.3`
    
2. For the following codes:

     ```apache
    profileDir = r"--user-data-dir=C:\Users\Chan\AppData\Local\Microsoft\Edge\User Data"
    ```

    * You should modify the path to your own browser's cache path.
    * Note that there are small but fatal difference between browsers'(e.g., IE, Chrome, Edge, Opera...) initialization with Selenium. You may search the method on the Internet.

    * The downloading process uses `ThreadPoolExecutor` from `cuncurrent.futures`. Fast, accurate and energy-saving.
  
3. Because of hurriedness, the coding style is not very uniform and sometimes might cause confusion. At some vital points, I've tried to seperate code snippets to make things clear. Anyway, I would never spare my apologies for any problems caused.

## Instuctions of the program itself

1. A new folder named "LSP" must be firstly present in the program's current folder.

2. All primary folder is named after illustrators, and all secondary ones are seperated with "Restricted"(R) and "Not-Restricted"(NR), and the pictures are crawled from the first page, with the same series identified with "_serial" ending.

3. If your connection is bad, you may moderately increase the time the progrm sleeps by adjusting the number in the brackets of `time.sleep()`.

4. When querying illusts and opening Edge processes, the program runs single-threadedly. That's because, firstly, the program must know which illust code matches with which  certain illust, and secondly, opening Edge processes is both network-expensive and RAM-expensive, and I at least want my program less RAM-costly. 

5. Some basic methods to test whether the program is running well:

    * Change multiprocessing to single-processing. It makes mulfunctioning parts raise errors.
    * Arbitrarily check if R and NR pics have been misplaced.
    * Use breakpoints.

6. The program is not necessarily up to date. Because pixiv sometimes changes its url format, at that time the strings in the program must be simultaneously updated.

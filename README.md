# ***ʹ��˵��***

## ���ڳ���������������������

1. ��������ܱ�֤�ڱ��˵�������û��������绷�����������С�

`Anaconda 1.10.0 with Python 3.8, Visual Studio Code Debugee`

`Firefox 83.0, automated with Selenium 3.141.0`

�������绷�����⣺ǽ�ڣ�һ������VPN��

2. ���ڳ����е��¶δ��룺

```apache
profile_dir = r'C:\\Users\\chen\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\twtf6r6t.default-release'
profile = webdriver.FirefoxProfile(profile_dir)
driver = webdriver.Firefox(profile)
```

* �������е��ļ�·��Ϊ���Լ���������û������ļ��С�
* �����ʹ�õĲ���*���ߺ�83.0*��*����/����*�汾����ʹ��������������Ӧ����γ�ʼ�����ؼ���Ϊ��

`Selenium Chrome(���� IE/Firefox ���ڰ汾/Opera...)`

�﷨��ͬ��С�졣���ǣ��հ��ҵĹ��ߺ��Ĵ���������⣡

3. �������������ѧ�𣨱�˵�������js��xpath�ˣ���������python��������д�ͱȽϲִ٣��������˹������Ż���˳���Ż��˴���ṹ��û��ԭ���Ĵ���������ң������Ѿ��ڿ�ͷ�͹ؼ�λ�þ���ע����һЩ��ʾ����������������ţ��һ��ǽ�������������������վ�����Ҳο�������Ƚϼ���up��/csdn����Ա��ʵ�����룬�������ҵġ�

## �������һЩ˵��

1. �����������½�һ������Ϊ��LSP�����ļ��У��ڴ˳������ڵĸ�Ŀ¼�¡�

2. ���е�һ���ļ����Ի�ʦ���������������ļ��зֳ�R��NR��ͼƬ�����һҳ��ʼ��ȡ��ͬһͼ����ͼƬ�ԡ�_serial������ʽ������

3. png����ͼƬ����ʵ�⣬����referer֮���ƺ����������⡣��ˣ�ֱ��selenium������ɴ�ͼ�������Ҫ������ҳ�����Ҳ�������̫�죬��ˣ�png�ļ��ӳ�����Ʊ����jpg�ļ����öࡣ����������rurudo��25760573���͌m���ޤҤ�5444479����

4. ����������粻�ã������ʵ��ص���һЩ�ط���`time.sleep(secs)`�е�`secs`ֵ��������Ϊ����selenium���ݵĹ��ߺ��ƺ�����ȵ���ҳ��ȫ��ȡ��ɾͽ��к�������/�رձ�ǩҳ����Ȼ������������Chrome������Edge��֮�࣬����û��������⡣

5.�������Ƿ�����������debug���Ļ���������

* ��ͼƬ����Ƿ�������
* ��죬���Ƿ���R��NR����һ��������

* ���ڳ����������ϵ㡣

6. �����򲻱�֤��ʱ���¡�����pixiv�ƺ����л��̶�����ַ��ʾ��ʽ��������Ҫ��ʱ�������е�һЩ�����ַ�������������������������Ŀǰ�����С�

# ***Program Instructions***

## About compatibility and coding style

1. The program can only be guaranteed to perform normally in my OWN coding, parsing, and network environment.

`Anaconda 1.10.0 with Python 3.8, Visual Studio Code Debugee`

`Firefox 83.0, automated with Selenium 3.141.0`

2. For the following codes:

```apache
profile_dir = r'C:\\Users\\chen\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\twtf6r6t.default-release'
profile = webdriver.FirefoxProfile(profile_dir)
driver = webdriver.Firefox(profile)
```

* You should modify the path to your own browser's cache path.
* Note that there are small but fatal difference between browsers'(e.g., IE, Chrome, Edge, Opera...) initialization with Selenium. You may search the method on the Internet.

3. Because of hurriedness, the coding style is not very uniform and sometimes might cause confusion. At the beginning and some vital points, I've tried my best to add some annotations to make things clear. Anyway, I would never spare my apologies for any problems caused.

## Instuctions of the program itself

1. A new folder named "LSP" must be firstly present in the program's current folder.

2. All primary folder is named after illustrators, and all secondary ones are seperated with "Restricted"(R) and "Not-Restricted"(NR), and the pictures are crawled from the last page, with the same series identified with "_serial" ending.

3. In the field test, .png file urls seems to sometimes deny my request(403) even with the illustrator's homepage referrer. So I have to use Selenium to click it open, which involves waiting the webpage open and clicking to zoom the picture. This is why, from the perspective of the program design, crawling down pngs is much slower than jpgs. (Take rurudo(25760573) and �m���ޤҤ�(5444479) for example!)

4. If your connection is bad, you may moderately increase the time the progrm sleeps by adjusting the number in the brackets of `time.sleep()`.

5. Some basic methods to test whether the program is running well:

* Check if the serial numbers of the pics are consecutive.
* Arbitrarily check if R and NR pics have been misplaced.

* Use breakpoints.

6. The program is not necessarily up to date. Because pixiv sometimes changes its url format and at that time, the strings in the program must be simultaneously updated.

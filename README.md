# yiban
易班涮网薪

selenium打开网页下载与安装方法
#
还有Edge的

下载地址
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/


将下载下来的GeckoDriver.exe放入python安装路径下

C:\Users\Administrator\AppData\Local\Programs\Python\Python310

其实就是放在python安装的路径上

#


 以Firefox（火狐）浏览器为例，安装其驱动Geckodriver

下载Geckodriver

下载地址：https://github.commozillageckodriverreleases


将下载下来的GeckoDriver.exe放入python安装路径下

C:\Users\Administrator\AppData\Local\Programs\Python\Python310

其实就是放在python安装的路径上



#
 python中常用selenium爬取动态渲染网页，这个过程之中需要安装浏览器驱动，这次以Google浏览器为例，安装其驱动chromedriver
这个Google的
chromedriver下载地址：
http://chromedriver.storage.googleapis.com/index.html

http://npm.taobao.org/mirrors/chromedriver/

两个地址都可以下载，根据自己的chrome浏览器的版本选择下载即可

查看浏览器版本



把exe文件复制到浏览器的安装目录下：C:\Users\Administrator\AppData\Local\Google\Chrome\User Data

C:\Users\Administrator\AppData\Local\Programs\Python\Python310

我是两个路径都放了

按照自己的电脑安装路径


配置环境变量:此电脑→右击属性→高级系统设置→环境变量→用户变量→Path→编辑→新建，将以下路径复制,然后不要忘记后续全部点击确定

C:\Users\Administrator\AppData\Local\Programs\Python\Python310



打开pycharm,输入以下代码，测试一下是否驱动成功

from selenium import webdriver

driver = webdriver.Chrome()

url = 'https://www.csdn.net/'

driver.get(url)

driver.maximize_window()



有些好像可以直接在pycharm的pip直接下载

#大学生需要涮网薪的这个脚本一天160网薪
#脚本后一半删除了
#需要请联系


from selenium.webdr
from selenium.webdriver
from selenium.webdriver.
from selenium.webdriver.c
from time import slee
import pyautogui

class Main:
    # 初始化，用Edge打开浏览器和易班登陆页
    def initWebkit(self):
        self.browse
        self.browser.ge
        #self.browser.m
    # 登陆易班进入首页
    def loginModel(self):
        #登录账号
        username = ''
        #密码
        password = ''
        self.browser.find_element(By
        self.browser.find_eleme
        self.browser.find_element(B
        sleep(3)
        try:
            self.browser.find_ele
            input('是否继续')
            self.browser.find_eleme
        except:
            print('直接进入首页')
    # 签到1
    def signInModel(self):
        try:
            WebDriverWait(self.browser, 20
            self.browser.find_element(By.I
            WebDriverWait(self.browser, 3, 0.5).
            #self.browser.find_element_by_xpath("//
            self.browser.find_element(By.XPATH,"
            self.browser.find_element(By.CS
        except:
            print('第一个签到完成')
    #签到2
    def signInModel2(self):
        self.browser.get('https://ww
        sleep(5)
        self.browser.find_element(By.XPAT
        print('第二个签到完成')
        sleep(2)
    # 发布微社区
    def publishBlogModel(self):
        i = 0
        while i < 20:
            self.browser.implicitly_wait(3)
            self.browser.get('https://s.
            title = '每日好句'#标题
            text = '喜欢白色，单纯，天真'#内容
            self.browser.find_element(By.XPATH
            sleep(2)
            self.browser.switch_to.frame('ueditor_0')
            self.browser.find_element(By.XPATH, "/
            self.browser.switch_to.de
            sleep(3)
            self.browser.find_element(By.XPATH, "/html/b
            i += 1
            sleep(65)
            print("发布完成第", i, "次")

    # 发布评论
    def pulishTrendsModel(self):
        self.browser.implicitly_wait(3)
        self.browser.get('https://s.yiban.
        i = 0
        while i < 31:
            self.browser.refresh()
            sleep(2)
            comment = '赞赞赞赞赞'#评论
            self.browser.find_element(By.XPATH, "//div
            self.browser.find_element(By.XPATH, "//input
            self.browser.find_element(By.XPATH, "//
            i += 1
            sleep(65)
            print("评论完成第", i, "次")

    # 点赞
    def changeInformationModel(self):
        self.browser.implicitly_wait(3)
        self.browser.get('https://s.yiban.cn/app
        self.browser.find_element(By.XPATH, "//div
        self.browser.find_element(By.XPATH, "//input[@type='
        self.browser.find_element(By.XPATH, "//div[
        i = 0
        while i < 31:
            sleep(2)
            js = 'window.scrol
            self.browser.execu
            sleep(0.5)
            self.browser.find_element(By.XPA
            i += 1
            sleep(4)
            print("点赞完

if __name__ == '__main__':
    m = Main()  # 声明主类
    m.initW # 打开浏览器
    m.logi  # 登陆易班
    m.signI # 签到
#     m.signIn    #签到2
#     m.publishB()  # 发布话题
#     m.pulishTren)  # 发布评论
#     m.changeInform) #点赞
    m.browse#关闭所有关联窗口，并且安全关闭session。
pyautogui.





    # 对应的find_element()方法具体如下
    # find_element(By.ID, "sb_form_go")；
    # find_element(By.CLASS_NAME, "b_searchboxSubmit")；
    # find_element(By.NAME, "go")；
    # find_element(By.CSS_SELECTOR, ".b_searchboxSubmit")；
    # find_element(By.XPATH, "//*[@id='sb_form_go']")；
    # find_element(By.LINK_TEXT, "")
    # 由于搜素框元素没有Link
    # text，所以对用属性值用替代；
    # find_element(By.PARTIAL_LINK_TEXT, "****")；
    # find_element(By.TAG_NAME, "****") 。

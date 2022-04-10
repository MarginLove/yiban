from selenium.webdriver import Edge
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui

class Main:
    # 初始化，用Edge打开浏览器和易班登陆页
    def initWebkit(self):
        self.browser = Edge()#指向使用Edge
        self.browser.get('https://www.yiban.cn/login')
        #self.browser.minimize_window()#会导致点赞识别不了
    # 登陆易班进入首页
    def loginModel(self):
        #登录账号
        username = ''
        #密码
        password = ''
        self.browser.find_element(By.ID, "account-txt").send_keys(username)
        self.browser.find_element(By.ID, "password-txt").send_keys(password)
        self.browser.find_element(By.ID, "login-btn").click()
        sleep(3)
        try:
            self.browser.find_element(By.CSS_SELECTOR, ".captcha")
            input('是否继续')
            self.browser.find_element(By.ID, "login-btn").click()
        except:
            print('直接进入首页')
    # 签到1
    def signInModel(self):
        try:
            WebDriverWait(self.browser, 20, 0.5).until_not(EC.presence_of_element_located((By.ID, 'tool-newbie')))
            self.browser.find_element(By.ID, "tool-sign").click()
            WebDriverWait(self.browser, 3, 0.5).until(EC.visibility_of_element_located((By.ID, 'sign-survey')))
            #self.browser.find_element_by_xpath("//div[@id='sign-survey']/dl/dd[1]/i").click()#老式写法
            self.browser.find_element(By.XPATH,"//div[@id='sign-survey']/dl/dd[1]/i").click()
            self.browser.find_element(By.CSS_SELECTOR, ".dialog-confirm").click()
        except:
            print('第一个签到完成')
    #签到2
    def signInModel2(self):
        self.browser.get('https://www.yibanyun.cn/app/sign')
        sleep(5)
        self.browser.find_element(By.XPATH, "//div[@class='signBtn']").click()
        print('第二个签到完成')
        sleep(2)
    # 发布微社区
    def publishBlogModel(self):
        i = 0
        while i < 20:
            self.browser.implicitly_wait(3)
            self.browser.get('https://s.yiban.cn/articles/detail')
            title = '每日好句'#标题
            text = '喜欢白色，单纯，天真'#内容
            self.browser.find_element(By.XPATH, "/html/body/div[1]/section/div[2]/div[2]/div/input").send_keys(title)
            sleep(2)
            self.browser.switch_to.frame('ueditor_0')
            self.browser.find_element(By.XPATH, "//body[@class='view' and @style='cursor: text;']").send_keys(text)
            self.browser.switch_to.default_content()
            sleep(3)
            self.browser.find_element(By.XPATH, "/html/body/div[1]/section/div[3]/div/button[2]/div").click()
            i += 1
            sleep(65)
            print("发布完成第", i, "次")

    # 发布评论
    def pulishTrendsModel(self):
        self.browser.implicitly_wait(3)
        self.browser.get('https://s.yiban.cn/app/2004230/post-detail/JqOhKBoKewnDZYJ')
        i = 0
        while i < 31:
            self.browser.refresh()
            sleep(2)
            comment = '赞赞赞赞赞'#评论
            self.browser.find_element(By.XPATH, "//div[@class='input-trigger']").click()
            self.browser.find_element(By.XPATH, "//input[@type='text' and @placeholder='写下评论...']").send_keys(comment)
            self.browser.find_element(By.XPATH, "//div[@class='submit-btn btn']").click()
            i += 1
            sleep(65)
            print("评论完成第", i, "次")

    # 点赞
    def changeInformationModel(self):
        self.browser.implicitly_wait(3)
        self.browser.get('https://s.yiban.cn/app/2001376/post-detail/7J0FArL69ZVDlR2')
        self.browser.find_element(By.XPATH, "//div[@class='input-trigger']").click()
        self.browser.find_element(By.XPATH, "//input[@type='text' and @placeholder='写下评论...']").send_keys('赞赞赞赞赞')
        self.browser.find_element(By.XPATH, "//div[@class='submit-btn btn']").click()
        i = 0
        while i < 31:
            sleep(2)
            js = 'window.scrollBy(0,1000)'
            self.browser.execute_script(js)
            sleep(0.5)
            self.browser.find_element(By.XPATH, "//*[@viewBox='0 0 24 20' and @class='svg-icon']").click()
            i += 1
            sleep(4)
            print("点赞完成第", i, "次")

if __name__ == '__main__':
    m = Main()  # 声明主类
    m.initWebkit()  # 打开浏览器
    m.loginModel()  # 登陆易班
    m.signInModel()  # 签到
    m.signInModel2()    #签到2
    m.publishBlogModel()  # 发布话题
    m.pulishTrendsModel()  # 发布评论
    m.changeInformationModel() #点赞
    m.browser.quit()#关闭所有关联窗口，并且安全关闭session。
pyautogui.alert(text='一天的网薪涮完了', title='python脚本运行状况')





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

from selenium import webdriver
from selenium.webdriver import Edge
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
js="window.open('{}','_blank');"





class Main:

    # 初始化，打开浏览器和易班登陆页
    def initWebkit(self):
        self.browser = Edge()
        #self.browser.implicitly_wait(10)
        self.browser.get('https://www.yiban.cn/login')
        #pyautogui.hotkey('f11')
    #登陆易班进入首页
    def loginModel(self):
        self.browser.find_element_by_id("account-txt").send_keys('15016429998')
        self.browser.find_element_by_id("password-txt").send_keys('Margin77')
        self.browser.find_element_by_id("login-btn").click()
        sleep(3)
        try:
            captcha_img = self.browser.find_element_by_css_selector(".captcha")
            str = input('是否继续')
            self.browser.find_element_by_id("login-btn").click()
        except:
            print('直接进入首页')

    #签到
    def signInModel(self):
        try:
            WebDriverWait(self.browser, 20, 0.5).until_not(EC.presence_of_element_located((By.ID, 'tool-newbie')))
            self.browser.find_element_by_id("tool-sign").click()
            WebDriverWait(self.browser, 3, 0.5).until(EC.visibility_of_element_located((By.ID, 'sign-survey')))
            self.browser.find_element_by_xpath("//div[@id='sign-survey']/dl/dd[1]/i").click()
            self.browser.find_element_by_css_selector(".dialog-confirm").click()
        except:
            return True


    # #发布
    # def publishBlogModel(self):
    #     try:
    #         WebDriverWait(self.browser, 20, 0.5).until(EC.element_to_be_clickable((By.ID, 'y-publish')))
    #         self.browser.find_element_by_id("y-publish").click()  # 点击发布按钮
    #         self.browser.find_element_by_id("i-publish").click()
    #     except:
    #         return True

    def tougao(self):
        self.browser.execute_script(js.format('https://s.yiban.cn/userPost/detail'))
        #self.browser.switch_to.window(self.window_handles[-1])

        sleep(5)

        self.browser.find_element_by_xpath("/html/body/div[1]/section/div[2]/div[1]/div/input").click()
        self.browser.find_element_by_xpath("/html/body/div[1]/section/div[2]/div[1]/div/input").click()
        self.browser.find_element_by_xpath("/html/body/div[1]/section/div[2]/div[1]/div/input']").send_keys('111222')
        self.browser.find_element_by_xpath("/html/body/div[1]/section/div[2]/div[1]/div/input").send_keys('111222')


if __name__ == '__main__':
    m = Main()  # 声明主类
    m.initWebkit()  # 打开浏览器
    m.loginModel()  # 登陆易班
    m.signInModel()  # 签到
   # m.publishBlogModel()  # 发布
    m.tougao()
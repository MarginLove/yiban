import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def login():
    global browser
    # 打开浏览器驱动
    browser = webdriver.Edge()  #浏览器对象
    # 隐身等待
    browser.implicitly_wait(3)
    # 打开易班网址
    browser.get('https://www.yiban.cn/')
    # 定位登录元素、并点击
    browser.find_element(By.XPATH, '//nav/div/div[2]/aside/span/a[2]').click()
    # 账号、密码
    account = ''
    password = ''
    # 定位账号元素
    browser.find_element(By.XPATH, '//main/div/div[2]/ul/li/div/input').send_keys(account)
    # 定位密码元素
    browser.find_element(By.XPATH, '//main/div/div[2]/ul/li/div[2]/input').send_keys(password)
    # 再次定位登录元素、并点击
    browser.find_element(By.XPATH, '//main/div/div[2]/ul/li/div[6]/a').click()
    time.sleep(1)

def sign_in1():
    time.sleep(1)
    # 定位签到元素
    browser.find_element(By.XPATH, "//li/i[@class='icon icon-sign guide2015_1-1']").click()
    # 定位选项
    time.sleep(1)
    browser.find_element(By.XPATH, "//div[@id='sign-survey' and @data-type='0']/dl/dd/i").click()
    # 定位完成
    time.sleep(1)
    browser.find_element(By.XPATH, "//a[@class='dialog-confirm' and @href='javascript:void(0)']").click()

def sign_in2():
    browser.get('https://www.yibanyun.cn/app/sign')
    browser.find_element(By.XPATH, "//div[@class='signBtn']").click()

def release():
    i = 0
    while i < 20:
        #打开发布页面
        browser.implicitly_wait(3)
        browser.get('https://s.yiban.cn/articles')
        browser.get('https://s.yiban.cn/articles/detail')

        gushi = '明月几时有，把酒问青天'
        browser.find_element(By.XPATH, "/html/body/div[1]/section/div[2]/div[2]/div/input").send_keys(gushi)
        time.sleep(1)
        browser.switch_to.frame('ueditor_0')    #从原本的主层定位到嵌套层里，就能定位到嵌套层里的元素；但是呢，使用完上面的方法后，就无法定位到原来主层元素
        browser.find_element(By.XPATH, "//body[@class='view' and @style='cursor: text;']").send_keys(gushi)
        browser.switch_to.default_content()
        # 确定投稿
        time.sleep(3)
        browser.find_element(By.XPATH, "/html/body/div[1]/section/div[3]/div/button[2]/div").click()
        i += 1
        time.sleep(65)

def comment():
    # 打开发布页面
    browser.implicitly_wait(3)
    browser.get('https://s.yiban.cn/app/2004230/post-detail/JqOhKBoKewnDZYJ')

    i=0
    while i<31:
        yuju='爱我中华，强我国家。'
        #刷新页面
        browser.refresh()
        time.sleep(2)
        browser.find_element(By.XPATH, "//div[@class='input-trigger']").click()
        browser.find_element(By.XPATH, "//input[@type='text' and @placeholder='写下评论...']").send_keys(yuju)
        browser.find_element(By.XPATH, "//div[@class='submit-btn btn']").click()
        i+=1
        time.sleep(65)

def like():
    # 打开发布页面
    browser.implicitly_wait(3)
    browser.get('https://s.yiban.cn/app/2001376/post-detail/7J0FArL69ZVDlR2')
    browser.find_element(By.XPATH, "//div[@class='input-trigger']").click()
    browser.find_element(By.XPATH, "//input[@type='text' and @placeholder='写下评论...']").send_keys('赞赞赞赞赞')
    browser.find_element(By.XPATH, "//div[@class='submit-btn btn']").click()
    i = 0
    while i < 31:
        time.sleep(2)
        js = 'window.scrollBy(0,1000)'
        browser.execute_script(js)
        time.sleep(0.5)
        browser.find_element(By.XPATH, "//*[@viewBox='0 0 24 20' and @class='svg-icon']").click()
        i += 1
        time.sleep(4)

if __name__ == '__main__':
    login()  # 登录
    sign_in1()  # 官网页面签到
    sign_in2()  # 易伴云签到
    release()  # 发布
    comment()   #评论
    like()      #点赞
    browser.quit()  #释放资源，退出浏览器

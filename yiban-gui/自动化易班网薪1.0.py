import pyautogui  # opencv
import time
import webbrowser

'''窗口最大化'''

webbrowser.open('https://www.yiban.cn/')  # 打开网站

#click1 = pyautogui.locateOnScreen('D:\\Python text\\python-GUI\\yiban-gui\\6.png')  # 点击，获取焦点
pyautogui.moveTo(100,300,duration=1)
#pyautogui.click(click1), \
pyautogui.hotkey('f11')  # 打开全窗口

'''登录功能'''

time.sleep(1)  # 延迟1s
enter_1 = pyautogui.locateOnScreen("D:\\Python text\\python-GUI\\yiban-gui\\1.png",
                                   confidence=0.6)  # 登录,con 过滤弱检测的最小概率,路径不能有中文
pyautogui.moveTo(enter_1), pyautogui.click(enter_1)  # click登录图形

time.sleep(1)  # 延迟1s
enter_2 = pyautogui.locateOnScreen("D:\\Python text\\python-GUI\\yiban-gui\\2.png", confidence=0.5)
pyautogui.moveTo(enter_2), pyautogui.click(enter_2)  # 再次click登录图形

'''签到功能'''
time.sleep(1)
pyautogui.moveTo(2508, 539), pyautogui.click(2508, 539)  # 点击签到

time.sleep(1)
qiandao1 = pyautogui.locateOnScreen("D:\\Python text\\python-GUI\\yiban-gui\\7.png", confidence=0.5)  # 签到选项
pyautogui.moveTo(qiandao1), pyautogui.click(qiandao1)

time.sleep(2)
qiandao2 = pyautogui.locateOnScreen("D:\\Python text\\python-GUI\\yiban-gui\\8.png", confidence=0.6)  # 完成签到
pyautogui.moveTo(qiandao2), pyautogui.click(qiandao2)

webbrowser.open("https://www.yibanyun.cn/app/sign")  # 打开另一个签到网页
time.sleep(2)
pyautogui.moveTo(1276, 191), pyautogui.click(1276, 191)  # 点击签到

'''评论功能'''
webbrowser.open("https://s.yiban.cn/app/2000064/post-detail/W3eiM2Y426LQRED")  # 打开网址

time.sleep(1)  # 延迟1s

i = 30
while i > 0:  # 评论循环30次
    time.sleep(1)
    pyautogui.moveTo(884, 1555), pyautogui.click(884, 1555)  # 点击评论条
    pyautogui.write("en,en,en,en")
    i -= 1
    pyautogui.moveTo(2525, 1560), pyautogui.click(2525, 1560)  # click发送图形，16英寸的
    time.sleep(70)  # 延迟70s

"""点赞"""
webbrowser.open("https://s.yiban.cn/app/2002260/post-detail/3JfpdopW6lnQWQ")  # 打开网址

time.sleep(1)  # 延迟1s
pyautogui.scroll(-11000)  # 向下滚动

a = -40
i = 0
while i < 31:  # 点赞循环，滚动循环31次
    good = pyautogui.locateOnScreen("D:\\Python text\\python-GUI\\yiban-gui\\5.png", confidence=0.5)
    pyautogui.moveTo(good), pyautogui.click(good)

    pyautogui.scroll(a)  # 滚动鼠标
    i += 1
    a += -40
    time.sleep(6)  # 延迟6s

"""发帖"""
webbrowser.open('https://www.yiban.cn/')
time.sleep(2)
pyautogui.moveTo(1935, 52), pyautogui.click(1935, 52)  # 移动发布位置，并点击
pyautogui.moveTo(1812, 167), pyautogui.click(1812, 167)  # 移动 微社区 位置，并点击
pyautogui.moveTo(2117, 45), pyautogui.click(2117, 45)
time.sleep(2)
pyautogui.moveTo(2117, 45), pyautogui.click(2117, 45)

i = 20
while i > 0:  # 评论循环20次
    time.sleep(2)
    pyautogui.moveTo(534, 119), pyautogui.click(534, 119)  # 点击评论条
    pyautogui.write("cqmyg,", 0.25)

    pyautogui.moveTo(715, 640), pyautogui.click(715, 640)  # 点击评论条
    pyautogui.write("ysdss,", 0.25)

    i -= 1
    pyautogui.moveTo(2155, 1548), pyautogui.click(2155, 1548)  # click发送图形，16英寸的

    pyautogui.moveTo(597, 93), pyautogui.click(597, 93)  # 获取焦点
    time.sleep(2)
    pyautogui.moveTo(597, 93), pyautogui.click(597, 93)  # 回到发布编辑界面
    time.sleep(70)  # 延迟70s

webbrowser.open("D:\\Python text\\python-GUI\\yiban-gui\\end.txt")  # 结束提示

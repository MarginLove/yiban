import pyautogui  # opencv
import time
from selenium import webdriver
js="window.open('{}','_blank');"

driver=webdriver.Edge()
driver.get(r'https://www.yiban.cn/login')
time.sleep(2)
pyautogui.hotkey('f11')
driver.find_element_by_id("account-txt").send_keys('17806702715')#账号
driver.find_element_by_id("password-txt").send_keys('jy020103')#密码
driver.find_element_by_id("login-btn").click()
time.sleep(2)

pyautogui.moveTo(1880,354), pyautogui.click(1880,354)
time.sleep(2)
pyautogui.moveTo(322,537), pyautogui.click(322,537)
time.sleep(2)
pyautogui.moveTo(1349,751), pyautogui.click(1349,751)
time.sleep(2)

# 打开另一个签到网页# 点击签到
driver.execute_script(js.format('https://www.yibanyun.cn/app/sign'))
time.sleep(2)
pyautogui.moveTo(960,183), pyautogui.click(960,183)  # 点击签到
time.sleep(2)

# '''评论功能'''
driver.execute_script(js.format('https://s.yiban.cn/app/2000064/post-detail/W3eiM2Y426LQRED'))
time.sleep(1)  # 延迟1s
i = 30
while i > 0:  # 评论循环30次
    time.sleep(1)
    pyautogui.moveTo(628,1048), pyautogui.click(628,1048)  # 点击评论条
    pyautogui.write("en,en,en,en", 0.25)
    i -= 1
    pyautogui.moveTo(1893,1046), pyautogui.click(1893,1046)
    time.sleep(65)

# """发帖"""
driver.execute_script(js.format('https://s.yiban.cn/userPost/detail'))
time.sleep(2)
i = 20# 评论循环20次
while i > 0:
    time.sleep(2)# 延迟2s
    pyautogui.moveTo(491,158), pyautogui.click(491,158)  # 点击评论条
    pyautogui.write("cqmyg,", 0.25)
    pyautogui.moveTo(445,546), pyautogui.click(445,546)  # 点击评论条
    pyautogui.write("ysdss,", 0.25)
    i -= 1
    pyautogui.moveTo(1682,1029), pyautogui.click(1682,1029)
    time.sleep(2)# 延迟2s
    pyautogui.moveTo(391,134), pyautogui.click(391,134)
    time.sleep(2)       # 延迟2s
    pyautogui.moveTo(557,159), pyautogui.click(557,159)  # 回到发布编辑界面
    time.sleep(65)  # 延迟70s
pyautogui.alert(text='一天的网薪涮完了', title='python脚本运行状况')












#
# import pyautogui  # opencv
# import webbrowser
# import time
#
#
# webbrowser.open('https://www.yiban.cn/')  # 打开网站
# pyautogui.moveTo(100,300,duration=1)     #点击像素点
# pyautogui.hotkey('f11')     #F11打开全屏
#
# #登录
# #这些像素点是用pyautogui.mouseInfo()来的
# time.sleep(1)
# pyautogui.moveTo(1525,45), pyautogui.click(1525,45)
# time.sleep(1)
# pyautogui.moveTo(1031,391), pyautogui.click(1031,391)
# pyautogui.typewrite('')
# time.sleep(1)
# pyautogui.moveTo(1047,465), pyautogui.click(1047,465)
# pyautogui.typewrite('')
#
# time.sleep(1)
# pyautogui.moveTo(1210,614), pyautogui.click(1210,614)
#
# '''签到功能'''
#
# # 打开另一个签到网页# 点击签到
# webbrowser.open("https://www.yibanyun.cn/app/sign")#签到页面
# time.sleep(2)
# pyautogui.moveTo(960,116), pyautogui.click(960,116)  # 点击签到
#
# '''评论功能'''
# webbrowser.open("https://s.yiban.cn/app/2000064/post-detail/W3eiM2Y426LQRED")  # 打开网址
# time.sleep(1)  # 延迟1s
#
# i = 30
# while i > 0:  # 评论循环30次
#     time.sleep(1)
#     pyautogui.moveTo(628,1048), pyautogui.click(628,1048)  # 点击评论条
#     pyautogui.write("en,en,en,en")
#     i -= 1
#     pyautogui.moveTo(1893,1046), pyautogui.click(1893,1046)
#     time.sleep(65)
#
# """发帖"""
# webbrowser.open('https://www.yiban.cn/')
# time.sleep(2)
# pyautogui.moveTo(1515,48), pyautogui.click(1515,48)  # 移动发布位置，并点击
# pyautogui.moveTo(1396,147), pyautogui.click(1396,147)  # 移动 微社区 位置，并点击
# pyautogui.moveTo(1666,39), pyautogui.click(1666,39)
# time.sleep(2)# 延迟2s
# pyautogui.moveTo(1666,39), pyautogui.click(1666,39)
#
# i = 20# 评论循环20次
# while i > 0:
#     time.sleep(2)# 延迟2s
#     pyautogui.moveTo(444,105), pyautogui.click(444,105)  # 点击评论条
#     pyautogui.write("cqmyg,", 0.25)
#
#     pyautogui.moveTo(445,546), pyautogui.click(445,546)  # 点击评论条
#     pyautogui.write("ysdss,", 0.25)
#
#     i -= 1
#     pyautogui.moveTo(1682,1029), pyautogui.click(1682,1029)
#     time.sleep(2)# 延迟2s
#     pyautogui.moveTo(391,75), pyautogui.click(391,75)
#     time.sleep(2)       # 延迟2s
#     pyautogui.moveTo(597, 93), pyautogui.click(597, 93)  # 回到发布编辑界面
#     time.sleep(70)  # 延迟70s
#
# pyautogui.alert(text='一天的网薪涮完了', title='python脚本运行状况')
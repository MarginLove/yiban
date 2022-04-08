from selenium import webdriver
import time
js="window.open('{}','_blank');"

driver=webdriver.Edge()
driver.get(r'https://www.yiban.cn/login')
time.sleep(2)


driver.find_element_by_id("account-txt").send_keys('17376579036')
driver.find_element_by_id("password-txt").send_keys('qq13931975931')
driver.find_element_by_id("login-btn").click()
driver.execute_script(js.format('https://s.yiban.cn/articles/detail'))
#driver.switch_to.window(driver.window_handles[-1])
time.sleep(2)

driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/div[2]/div/input').send_keys('111222')












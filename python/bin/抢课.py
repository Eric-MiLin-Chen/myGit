#!usr/bin/python
#-*- coding: GBK -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

account = input('请输入学号：')
password = input('请输入密码：')
classes = []

while True:
    tmp = input('请输入（课程号 教师号）与回车，以0作为输入完毕：').split()
    if tmp == ['0']:
        break
    else:
        classes.append(tmp)

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])#禁止打印日志
driver = webdriver.Chrome(options=chrome_options)
sleep(1)
driver.get('http://xk.autoisp.shu.edu.cn/')
sleep(1)
input("请输入回车以开始选课...")
driver.find_element(By.ID, "username").send_keys(account)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.XPATH, '//button[text() = "登录"]').click()
driver.find_element(By.NAME, 'rowterm').click()
driver.find_element(By.XPATH, '//span[text() = "确定"]').click()

for i in classes:
    # driver.find_element(By.XPATH, '//span[text() = "选课"]').click()
    # driver.find_element(By.XPATH, '//button[@type = "submit"]').click()
    driver.find_element(By.XPATH, '//*[@id = "CourseSelectionStudentFuzzyQuery"]').click()
    driver.find_element(By.XPATH, '//*[@name = "CID"]').send_keys(i[0])
    driver.find_element(By.XPATH, '//*[@name = "TeachNo"]').send_keys(i[1])
    driver.find_element(By.XPATH, '//button[@id="QueryAction"]').click()
    driver.find_element(By.XPATH, '//*[@name = "checkclass"]').click()
    driver.find_element(By.XPATH, '//button[@id = "CourseCheckAction"]').click()
    driver.find_element(By.XPATH, '//span[text() = "关闭"]').click()
    sleep(0.5)
input("选课结束！（按回车以退出）")

driver.quit()
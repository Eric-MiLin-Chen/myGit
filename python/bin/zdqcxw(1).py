from time import sleep
from selenium import webdriver
wd = webdriver.Chrome(r'chromedriver.exe')
wd.get('https://i.chaoxing.com')
sleep(1)
wd.find_element_by_id('phone').send_keys('手机号')
wd.find_element_by_id('pwd').send_keys('密码')
wd.find_element_by_id('loginBtn').click()
sleep(1)
wd.get('http://auth.chaoxing.com/connect/oauth2/authorize?appid=f4ce4d9db82446afbafd3a4e572b06a4&redirect_uri=http%3A%2F%2Foffice.chaoxing.com%2Ffront%2Fweb%2Fmicro%2Fapi%2Fgopage%3FbackUrl%3Dhttp%253A%252F%252Foffice.chaoxing.com%252Ffront%252Fweb%252Fapps%252Fforms%252Ffore%252Fapply%253Fid%253D9045%2526formAppId%253D%2526enc%253D14a275030e8f420727b7765ad6a48301%26appId%3Df4ce4d9db82446afbafd3a4e572b06a4%26appKey%3Dj1D7j81YsQJH53sT%26uid%3D129409239%26mappId%3D5291671%26from_type%3Dspace%26fidEnc%3D6c30e7d3dd75783b&response_type=code&scope=snsapi_base&state=119727')
sleep(1)
wd.find_element_by_xpath("/html/body/div/div[2]/div[4]/div[2]/ul/div/ul/li[1]/div[3]/div[1]/i").click()
wd.find_element_by_xpath("/html/body/div/div[2]/div[4]/div[2]/ul/div/ul/li[4]/div[3]/div[1]/i").click()
wd.find_element_by_xpath("/html/body/div/div[2]/div[5]/div/div[2]/p").click()
sleep(1)
wd.find_element_by_xpath("/html/body/div/div[11]/div[2]/span[2]").click()
sleep(0.5)
wd.quit()
quit()

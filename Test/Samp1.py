from selenium import webdriver
from selenium
browser='chrome'
if(browser=='chrome'):
    driver =  webdriver.Chrome(executable_path='C:/Users/Roy/Downloads/Driver/chromedriver.exe')
elif(browser=='firefox'):
    driver = webdriver.Firefox(executable_path='C:/Users/Roy/Downloads/Driver/geckodriver.exe')
else:
    print("No browser path found")
driver.get('http://www.facebook.com')
driver.implicitly_wait(30)
driver.find_element_by_name("firstname").send_keys("Harish")
driver.find_element_by_name("lastname").send_keys("Qspider")
#driver.find_element_by_xpath("//input[contains(@//*[@id="u_0_q"]")

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

browser='chrome'
if(browser=='chrome'):
    driver =  webdriver.Chrome(executable_path='C:/Users/Roy/Downloads/Driver/chromedriver.exe')
elif(browser=='firefox'):
    driver = webdriver.Firefox(executable_path='C:/Users/Roy/Downloads/Driver/geckodriver.exe')
elif(browser=='IE'):
    driver = webdriver.InternetExplorer(executable_path='C:/Users/Roy/Downloads/Driver/IEDriverServer.exe')
else:
    print("No browser path found")

driver.get('http://www.facebook.com')
driver.implicitly_wait(30)
driver.find_element_by_name("firstname").send_keys("Test Name")
driver.find_element_by_name("lastname").send_keys("Test Surname")
#driver.find_element_by_xpath("//input[contains(@//*[@id="u_0_q"]")
driver.find_element_by_xpath("//*[@id='u_0_q']").send_keys("9876543210")
driver.find_element_by_xpath("//*[@id='u_0_x']").send_keys("Password@123")
driver.find_element_by_name("birthday_day").send_keys("24")
driver.find_element_by_id("month").send_keys("Mar")
driver.find_element_by_name("birthday_year").send_keys("1992")
driver.find_element_by_xpath("//input[@value='2']").click()
driver.find_element_by_name("websubmit").click()







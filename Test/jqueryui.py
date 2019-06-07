from selenium import webdriver
browser='chrome'
if(browser=='chrome'):
    driver =  webdriver.Chrome(executable_path='C:/Users/Roy/Downloads/Driver/chromedriver.exe')
elif(browser=='firefox'):
    driver = webdriver.Firefox(executable_path='C:/Users/Roy/Downloads/Driver/geckodriver.exe')
else:
    print("No browser path found")

driver.get("https://jqueryui.com/datepicker/#dropdown-month-year")
driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id="datepicker"]"]
framevar= driver.find_element_by_xpath("//iframe'[@class='demo-frame']")
driver.switch_to_frame(framevar)
driver.find_element_by_xpath("//input[@class='hasDatepicker']").click()
month=driver.find_element_by_class_name("ui-datepicker-month")
s1=Select(month)
s1.select_by_visible_text("Mar")
year=driver.find_element_by_class_name("ui-datepicker-year")
s2=Select(year)
s1.select_by_value("2010")
driver.











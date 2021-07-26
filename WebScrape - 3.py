from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.google.com/imghp')
search_field = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
search_field.send_keys('dog')
search_field.submit()
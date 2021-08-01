import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver

git_user = input('Enter Github User Name: ')
url = "https://github.com/"+git_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_img = soup.find('img', {'alt':'Avatar'})['src']
driver = webdriver.Chrome()
driver.get(profile_img)

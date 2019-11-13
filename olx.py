from bs4 import BeautifulSoup
from selenium import webdriver
import re
import requests
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

"""
For using this script, download gecko driver. 
"""
options = Options()
options.add_argument('--headless')
r = requests.get('https://www.olx.ua/')
soup = BeautifulSoup(r.text, 'html.parser')
a = soup.find_all('a', attrs = {'href': re.compile('https://www')})

obyavleniya = list()

for link in a:
    if 'obyavlenie' in link.get('href'):
        if not link.get('href') in obyavleniya:
            obyavleniya.append(link.get('href'))

n = 0

print(obyavleniya[n])
z = list()
driver = webdriver.Firefox(executable_path='C:\geckodriver\geckodriver.exe')
for single_page in obyavleniya:
    driver.get(single_page)
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@data-rel='phone']")))
    button = driver.find_element_by_xpath("//div[@data-rel='phone']")
    button.click()
    name = driver.find_element_by_xpath('/html/body/div[2]/section/div[3]/div/div[1]/div[2]/div/div[4]/div[2]/h4/a').text
    if '\n' in button.text:
        a = button.text.split('\n')
        z.append(a)
        z.append(name)
    else:
        z.append(button.text)
        z.append(name)
    print(z)

driver.quit()
from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver = webdriver.Firefox()

email = 'nathan.l.lee123@gmail.com'#raw_input('Email: ')
password = '3xFXwaK951od'#raw_input('Password: ')


driver.get('https://www.strava.com/athlete/training')

#signin
driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('login-button').click()
print('Signed in')
time.sleep(1.5)

#parse with bs


urllist = []
activitycounter = 0

while True:

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for activityurls in soup.find_all('a', {"data-field-name" : "name"}):
        url = activityurls['href']
        urllist.append(url)
        activitycounter += 1
    print('Found activities: ' + str(activitycounter))
    try:
        time.sleep(3)
        next_page_button = driver.find_element_by_class_name('next_page')
        next_page_button.click()
    except:
        print(urllist)
        break


print(str(len(urllist)) + ' Activities Found')

correctedcounter = 0
for urls in urllist:
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_id('distance-adjusted-help').click()

    try:
        driver.find_element_by_link_text('Correct Distance').click()
        print('Corrected Distance on: ' + urls)
        correctedcounter += 1
    except:
        print('Already Corrected: ' + urls)
        continue
print(str(correctedcounter) + ' / ' + str(len(urllist)) + 'Activities Corrected')

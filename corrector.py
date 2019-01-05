from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver = webdriver.Firefox()

email = raw_input('Email: ')
password = raw_input('Password: ')


driver.get('https://www.strava.com/athlete/training')

#signin
driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('login-button').click()

if driver.current_url == 'https://www.strava.com/athlete/training':
    print('Signed in')

time.sleep(1.5)



urllist = []
activitycounter = 0
pagecounter = 1
while True:

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # get urls
    for activityurls in soup.find_all('a', {"data-field-name" : "name"}):
        url = activityurls['href']
        print(url)
        urllist.append(url)
        activitycounter += 1

    print('Found activities: ' + str(activitycounter) + ' Page ' + 'pagecounter')

    # click button
    try:
        next_page_button = driver.find_element_by_class_name('next_page')
        next_page_button.click()
    except:
        print(urllist)
        break
    pagecounter += 1


print(str(len(urllist)) + ' Activities Found')

correctedcounter = 0
for urls in urllist:
    while driver.current_url != urls:
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
print(str(correctedcounter) + ' / ' + str(len(urllist)) + ' Activities Corrected')

from bs4 import BeautifulSoup
import requests
from robobrowser import RoboBrowser
import re
browser = RoboBrowser(history = True)
browser.open('https://www.strava.com/athlete/training')

email = browser.get_form(id='email')
email['q'].value = 'nathan.l.lee123@gmail.com'
password = browser.get_form(id='password')

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def extract_data_lele(url):

    content = requests.get(url)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # executable_path param is not needed if you updated PATH
    browser = webdriver.Chrome(options=options, executable_path='venv/chromedriver-Windows')
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, features="html.parser")
    browser.quit()

    products = {}
    # Find the main-shelf element
    objects = []
    a = soup.find('tbody')
    for tr in a.find_all('tr'):
        if (tr.find('a', class_='ajax1') is not None):
            ip_address = tr.find('a', class_='ajax1').text
            port = tr.find('span', class_='port').text
            objects.append({'ip_address': ip_address, 'port': port})

    print(objects)

    return products
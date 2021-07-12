from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
from random import randint

chrome_driver_path = "E:/Python/WebDriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Load the search page
url = "https://www.gumtree.com.au/s-desktops/c18551"
driver.get(url)

# Make Selenium and Chrome Webdriver look like a normal user and browser
ua = UserAgent()
random_header = ua.random

# headless Selenium, change boolean to True after testing
# with visuals or use driver to get screenshots
options = Options()
options.headless = False
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument(f'user-agent={random_header}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

# Find all anchor tags under the <section class="search-results-page__user-ad-collection">
items_anchor = driver.find_elements_by_xpath('/html/body/div[1]/div/div[3]/div/div[3]/main/section//a')

# Get a list of links from the <a> tags
list_href = []
for anchor in items_anchor:
    list_href.append(anchor.get_attribute('href'))

# Save the links in a file
file = "data/list_href.txt"
with open(file, mode="w", encoding="utf-8") as fp:
    for item in list_href:
        fp.write(f'{item}\n')


# Open the file containing links
file = "data/list_href.txt"
with open(file, mode="r", encoding="utf-8") as fp:
    list_href = fp.read().splitlines()
print(f'{list_href = }')


for href in list_href:
    driver.get(href)

    search_keywords = driver.find_element_by_xpath(
        '//*[contains(text(), \'GeForce\')]'
    )
    print(search_keywords)
    time.sleep(randint(3, 8))

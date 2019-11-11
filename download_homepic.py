#!/usr/bin/env python3

# After using selenium, I can only appreciate how much better puppeteer is when
# it comes to async, error handling and general syntax
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Considered using the imageio lib, but using requests seems better when it
# comes to something as trivial as downloading an image
import requests

# You need to change the path below to where chromedriver is located on your
# computer. You can download the chromedriver from
# https://chromedriver.chromium.org/
driver = webdriver.Chrome("./chromedriver")

driver.get("https://unsplash.com/")

try:
    image_src = driver.find_element_by_css_selector("#app picture > img") \
                      .get_attribute("src")

    picture_request = requests.get(image_src)
    if picture_request.status_code == 200:

        # At the moment, I just simply call it "image.jpg". Maybe we can have
        # sequential naming of files for consecutive runs?
        with open("image.jpg", 'wb') as f:
            f.write(picture_request.content)

except NoSuchElementException:
    print("Uh oh, could not find the home page image.")

driver.quit()

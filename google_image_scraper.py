import json
import os
import time
from urllib.parse import urlparse
import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shutil

class GoogleImageScraper():
    def __init__(self, config):
        options = Options()
        if config['headless']:
            options.add_argument('--headless')
        self.driver = webdriver.Chrome(executable_path=config['webdriver_path'], options=options)
        self.search_key = config['search_key']
        self.number_of_images = config['number_of_images']
        self.image_path = config['image_path']
        if not os.path.exists(self.image_path):
            os.makedirs(self.image_path)
        self.min_resolution = config['min_resolution']
        self.max_resolution = config['max_resolution']
        self.max_missed = config['max_missed']
        self.url = f"https://www.google.com/search?q={self.search_key}&tbm=isch"

    def reject_google_terms(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            reject_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div > div > div.NIoIEf > div.G4njw > div.AIC7ge > div.CxJub > div.VtwTSb > form:nth-child(1) > div > div > button')))
            reject_button.click()
        except Exception as e:
            print("[INFO] Google Terms rejection button not found.")

    def find_image_urls(self):
        print("[INFO] Gathering image links")
        self.driver.get(self.url)
        self.reject_google_terms()
        image_urls = []
        count = 0
        missed_count = 0
        indx = 0
        search_string = '//*[@id="islrg"]/div[1]/div[%d]/a[1]/div[1]/img'
        time.sleep(3)
        while self.number_of_images > count and missed_count < self.max_missed:
            indx += 1
            try:
                imgurl = self.driver.find_element(By.XPATH, search_string % indx)
                imgurl.click()
                time.sleep(1)
                class_names = ["n3VNCb", "iPVvYb", "r48jcc", "pT0Scc", "n4hgof"]

                for class_name in class_names:
                    images = self.driver.find_elements(By.CLASS_NAME, class_name)
                    if len(images) == 0:
                        continue

                    for image in images:
                        src_link = image.get_attribute("src")
                        response = requests.get(src_link, stream=True)

                        if response.status_code == 200:
                            response.raw.decode_content = True

                            with open(os.path.join(self.image_path, "image{}.jpg".format(count)), 'wb') as f:
                                shutil.copyfileobj(response.raw, f)

                            count += 1
                            missed_count = 0
                            break  # break out of the inner loop
                    else:  # this will be executed if the inner loop was not broken
                        continue  # continue to the next iteration of the outer loop

                    break  # break out of the outer loop

            except Exception as e:
                print(e)
                missed_count += 1
        
        self.driver.quit()
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

import time
import os
import shutil
import re

def main():
    #chop = webdriver.ChromeOptions
    
    uc.TARGET_VERSION = 97
    driver = uc.Chrome()
    
    
    
    #driver.get('https://video.ethz.ch/lectures/d-arch/2021/autumn/052-0505-00L.html')
    driver.get('https://video.ethz.ch/lectures.html')
    
    #  below code  get urls of mp4 elements https://video.ethz.ch/lectures.series-metadata.json 
    
    #from selenium.webdriver.common.by import By
    
    time.sleep(5)

    download_date = driver.find_elements(By.CSS_SELECTOR, 'time')[1].text
    #download_link = driver.find_element(By.CSS_SELECTOR, '.video a').get_attribute("href")
    
    print(download_date)
    #print(download_link)


#path = r
    time.sleep(10)







if __name__ == "__main__":
    main()

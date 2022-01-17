from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException

import time
import os
import shutil
import re

def main():
    uc.TARGET_VERSION = 97
    driver = uc.Chrome()
    
    # Get all departments with videos on the ETH video platform
    #scrape_departments(driver)
    
    # Get all years of a specific department
    scrape_years(driver, 'd-arch')
    
    time.sleep(10)


def scrape_departments(driver):
    driver.get('https://video.ethz.ch/lectures.html')
    
    # Get all link elements
    department_links = driver.find_elements(By.CSS_SELECTOR, '.newsListBox a')
    
    for department_link in department_links:
        department_href = department_link.get_attribute('href')
        print(department_href)



def scrape_years(driver, department):
    driver.get(f'https://video.ethz.ch/{department.lower()}.html')
    
    # Get all link elements
    years_links = driver.find_elements(By.CSS_SELECTOR, '.newsListBox a')
    
    for year_link in years_links:
        year_href = year_link.get_attribute('href')
        print(year_href)




if __name__ == "__main__":
    main()

#download_date = driver.find_elements(By.CSS_SELECTOR, 'time')[1].text
#download_link = driver.find_element(By.CSS_SELECTOR, '.video a').get_attribute("href")
#driver.get('https://video.ethz.ch/lectures/d-arch/2021/autumn/052-0505-00L.html')
#options = webdriver.FirefoxOptions()
#options.log.level = "trace"
#options.headless = True
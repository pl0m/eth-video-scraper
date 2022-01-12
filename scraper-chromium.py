from selenium import webdriver
from selenium.webdriver import Chrome
import undetected_chromedriver as uc

import time

def main():
    #chop = webdriver.ChromeOptions
    
    uc.TARGET_VERSION = 97
    driver = uc.Chrome()
    
    
    #
    driver.get('https://video.ethz.ch/')
    
    time.sleep(1000)







if __name__ == "__main__":
    main()

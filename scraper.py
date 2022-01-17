from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

class Scraper:
    def __init__(self):
        uc.TARGET_VERSION = 97
        self.driver = uc.Chrome()
    
    
    def scrape_departments(self):
        self.driver.get('https://video.ethz.ch/lectures.html')
        
        # Get all link elements
        department_links = self.driver.find_elements(By.CSS_SELECTOR, '.newsListBox a')
        
        for department_link in department_links:
            department_href = department_link.get_attribute('href')
            print(department_href)


    def scrape_years(self, department):
        self.driver.get(f'https://video.ethz.ch/lectures/{department.lower()}.html')
        
        # Get all link elements
        years_links = self.driver.find_elements(By.CSS_SELECTOR, '.newsListBox a')
        
        for year_link in years_links:
            year_href = year_link.get_attribute('href')
            print(year_href)
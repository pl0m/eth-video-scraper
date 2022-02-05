import os
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from storage import *
import undetected_chromedriver as uc

class Scraper:
    def __init__(self):
        uc.TARGET_VERSION = 97
        self.driver = uc.Chrome()
        
        # Check if we already have a storage.json file
        if os.path.isfile('storage.json') and os.access('storage.json', os.R_OK):
            self.store = StoragePool.load()
        else:
            self.store = StoragePool()
    
    def scrape_departments(self):
        self.driver.get('https://video.ethz.ch/lectures.html')
        
        # Get all link elements
        department_links = self.driver.find_elements(By.CSS_SELECTOR, '.newsListBox a')
        
        for department_link in department_links:
            department_href = department_link.get_attribute('href')
            department_name = department_href.rsplit('/', 1)[1].split('.')[0].upper()
            self.store.add_department(Department(department_name, department_href))


    def scrape_years(self, department):
        self.driver.get(f'https://video.ethz.ch/lectures/{department.lower()}.html')
        
        # Get all link elements
        years_links = self.driver.find_elements(By.CSS_SELECTOR, '.newsListBox a')
        
        for year_link in years_links:
            year_href = year_link.get_attribute('href')
            print(year_href)
        

    def scrape_semesters(self, department, year):
        self.driver.get(f'https://video.ethz.ch/lectures/{department.lower()}/{year}.html')
        
        # Get all link elements
        semesters_links = self.driver.find_elements(By.CSS_SELECTOR, '.newsListBox a')
        
        for semester_link in semesters_links:
            semester_href = semester_link.get_attribute('href')
            print(semester_href)
            
    def scrape_subjects(self, department, year, semester):
        self.driver.get(f'https://video.ethz.ch/lectures/{department.lower()}/{year}/{semester.lower()}.html')
        
        # Get all link elements
        subject_links = self.driver.find_elements(By.CSS_SELECTOR, '.newsListBox a')
        
        for subject_link in subject_links:
            subject_href = subject_link.get_attribute('href')
            subject_name = subject_link.find_element(By.CSS_SELECTOR, 'h2').text
            subject_lecturers = subject_link.find_element(By.CSS_SELECTOR, '.description').text
            print(f'{subject_name} is presented by {subject_lecturers}')
            
    def get_login_state(self):
        video_login_elements = self.driver.find_elements(By.CSS_SELECTOR, '#login')
        account_login_elements = self.driver.find_elements(By.CSS_SELECTOR, 'body.loggedin')
        if(len(account_login_elements) == 1):
            if(len(video_login_elements) == 1):
                return 1
            else:
                return 2
        else:
            return 0
        
    def save_to_file(self):
        self.store.save()
        
#   Elements for checking login status:
#    CSS Selector       Description
#    body.loggedin      User is logged in
#    #login             Video needs seperate password
#
#   States:
#    0  Not logged in and no access to video
#    1  Logged in but no access to video
#    2  Logged in and access to video


#download_date = driver.find_elements(By.CSS_SELECTOR, 'time')[1].text
#download_link = driver.find_element(By.CSS_SELECTOR, '.video a').get_attribute("href")
#driver.get('https://video.ethz.ch/lectures/d-arch/2021/autumn/052-0505-00L.html')
#options = webdriver.FirefoxOptions()
#options.log.level = "trace"
#options.headless = True

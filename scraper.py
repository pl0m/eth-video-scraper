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
            # Rebuild our storage structure from the file
            self.store = StoragePool.load()
        else:
            # Create a new storage structure
            self.store = StoragePool()
            
    # Oberfunktion
    def scrape_everything(self):
        # Scrapes all departments
        self.scrape_departments()
        
        # Iterates through our departments and scrapes their years
        for department in self.store:
            self.scrape_years(department)
        
        # First iterates through our departments
        for department in self.store:
            # Then iterates through their years and scrapes their semesters
            for year in department:
                self.scrape_semesters(year)
        
        # First iterates through our departments
        for department in self.store:
            # Then iterates through their years
            for year in department:
                # Then iterates through their semesters and scrapes their subjects
                for semester in year:
                    self.scrape_subjects(semester)
                    
    
    def scrape_departments(self):
        self.driver.get('https://video.ethz.ch/lectures.html')
        
        # Get all link elements
        department_links = self.driver.find_elements(By.CSS_SELECTOR, '.newsListBox a')
        
        for department_link in department_links:
            department_href = department_link.get_attribute('href')
            # Get name from link (split link from end by '/' and limit results to 1, then get the second [1] element)
            department_name = department_href.rsplit('/', 1)[1].split('.')[0].upper()
            # Add a new department to the storage pool
            self.store.add_department(Department(department_name, department_href))


    def scrape_years(self, department):
        self.driver.get(department.get_href())
        
        # Get all link elements
        years_links = self.driver.find_elements(By.CSS_SELECTOR, '.newsListBox a')
        
        for year_link in years_links:
            year_href = year_link.get_attribute('href')
            year_year = year_href.rsplit('/', 1)[1].split('.')[0]
            # Add a new year to the department
            department.add_year(Year(year_year, year_href))

    def scrape_semesters(self, year):
        self.driver.get(year.get_href())
        
        # Get all link elements
        semesters_links = self.driver.find_elements(By.CSS_SELECTOR, '.newsListBox a')
        
        for semester_link in semesters_links:
            semester_href = semester_link.get_attribute('href')
            semester_semester = semester_href.rsplit('/', 1)[1].split('.')[0].capitalize()
            year.add_semester(Semester(semester_semester, semester_href))
            
    def scrape_subjects(self, semester):
        self.driver.get(semester.get_href())
        
        # Get all link elements
        subject_links = self.driver.find_elements(By.CSS_SELECTOR, '.newsListBox a')
        
        for subject_link in subject_links:
            subject_href = subject_link.get_attribute('href')
            subject_name = subject_link.find_element(By.CSS_SELECTOR, 'h2').text
            subject_lecturers = subject_link.find_element(By.CSS_SELECTOR, '.description').text
            subject_id = subject_href.rsplit('/', 1)[1].split('.')[0]
            semester.add_subject(Subject(subject_name, subject_href, subject_id))
            
    def scrape_lectures(self, subject):
        self.driver.get(subject.get_href())
            
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

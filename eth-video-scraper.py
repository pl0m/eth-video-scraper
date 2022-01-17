import time
from scraper import Scraper

def main():
    
    scraper = Scraper()
    
    # Get all departments with videos on the ETH video platform
    #scraper.scrape_departments(driver)
    
    # Get all years of a specific department
    scraper.scrape_years('d-arch')
    
    time.sleep(10)




if __name__ == "__main__":
    main()

#download_date = driver.find_elements(By.CSS_SELECTOR, 'time')[1].text
#download_link = driver.find_element(By.CSS_SELECTOR, '.video a').get_attribute("href")
#driver.get('https://video.ethz.ch/lectures/d-arch/2021/autumn/052-0505-00L.html')
#options = webdriver.FirefoxOptions()
#options.log.level = "trace"
#options.headless = True
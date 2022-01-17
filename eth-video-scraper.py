import time
from scraper import Scraper

def main():
    # Create new instance of Scraper class
    scraper = Scraper()
    
    # Get all departments with videos on the ETH video platform
    #scraper.scrape_departments(driver)
    
    # Get all years of a specific department
    scraper.scrape_years('d-arch')
    
    # Wait for 10s before exiting
    time.sleep(10)




if __name__ == "__main__":
    main()

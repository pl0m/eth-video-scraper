import time
import json
from scraper import Scraper

from storage import Lecture


def main():
    # Create new instance of Scraper class
    scraper = Scraper()
    
    # Get all departments with videos on the ETH video platform
    scraper.scrape_everything()
    
    # Get all years of a specific department
    #scraper.scrape_years('d-arch')
    
    # Get all subjects of a specific department in a specific year and semester
    #scraper.scrape_subjects('d-arch', '2021', 'autumn')
    
    # Save scraped data to storage.json
    scraper.save_to_file()
    
    # Wait for 5s before exiting
    time.sleep(5)




if __name__ == "__main__":
    main()

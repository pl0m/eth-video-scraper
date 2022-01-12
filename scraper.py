from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.service import Service

options = webdriver.FirefoxOptions()
options.log.level = "trace"
#options.headless = True

capabilities = DesiredCapabilities.FIREFOX
capabilities["marionette"] = False

#driver = webdriver.Firefox(firefox_profile=profile, executable_path=GeckoDriverManager().install(), options=options)
#driver = webdriver.Firefox(executable_path=r'/opt/WebDriver/bin/geckodriver')
service = Service(executable_path="/opt/WebDriver/bin/geckodriver")
driver = webdriver.Firefox(service=service)

driver.get("http://www.google.com")

driver.get_screenshot_as_file("capture.png")
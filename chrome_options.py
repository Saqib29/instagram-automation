from selenium.webdriver.chrome.options import Options
import os


def chrome_options() -> Options:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    options = Options()
    # options.add_argument("--start-maximized")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    return options

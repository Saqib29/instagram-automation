from selenium.webdriver.chrome.options import Options


def chrome_options() -> Options:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    options = Options()
    # Don't change these options
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")
    return options

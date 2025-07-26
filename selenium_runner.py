# selenium_runner.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def run_browser():
    options = Options()
    options.add_argument("--proxy-server=http://127.0.0.1:8080")  # MITMProxy default
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    try:
        # Replace with the starter link you want to analyze
        driver.get("http://accounts.google.com/")
        time.sleep(60)  # Give yourself time to complete login manually
    finally:
        driver.quit()


if __name__ == "__main__":
    run_browser()

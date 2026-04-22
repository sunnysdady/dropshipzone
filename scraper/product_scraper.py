import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def fetch_product(url: str) -> dict:
    """抓取 1688 商品的核心信息，返回结构化 dict"""
    driver = get_driver()
    try:
        driver.get(url)
        # 等待商品核心信息出现（根据 1688 页面结构，可自行微调）
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-title")))
        title = driver.find_element(By.CSS_SELECTOR, ".product-title").text.strip()
        sku = driver.find_element(By.CSS_SELECTOR, ".product-sku").text.strip()
        price = driver.find_element(By.CSS_SELECTOR, ".price").text.strip()
        images = [
            img.get_attribute("src")
            for img in driver.find_elements(By.CSS_SELECTOR, ".product-image img")
        ]
        # 返回最基本的信息，后续可自行补全
        return {
            "name": title,
            "sku": sku,
            "price": price,
            "images": images,
        }
    finally:
        driver.quit()

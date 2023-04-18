from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome webdriver with headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# List of URLs to scrape
urls = [
    'https://www.avito.ma/fr/boutique?id=4203',
'https://www.avito.ma/fr/boutique?id=1688',
'list of Urls'
]

for url in urls:
    # Navigate to the webpage
    driver.get(url)

    # Find and click on the button element using the given class names
    button_class_names = 'button.sc-uoqswv-0.sc-uoqswv-1.sc-uoqswv-2.fhWmiT.dBNPnL'
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, button_class_names)))
    button.click()

    # Wait for the hidden text to appear and extract its text using the <span> tag
    hidden_text_xpath = '//*[@id="__next"]/div/main/div/div/div/div[1]/div[1]/div/div/div/div/a/span'
    hidden_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, hidden_text_xpath)))
    hidden_text_text = hidden_text.text

    print(hidden_text_text)

# Close the webdriver
driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import urllib.request

service = Service('C:\\Users\\FloMo\\Downloads\\chromedriver.exe')

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://rockpaperthis.com")
    return driver

def main():
    driver = get_driver()
    element = driver.find_element(by="xpath", value="/html/body/div[5]/div[1]/a/img")
    return element.get_attribute("src")

def download_image(url, save_path):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.00 Safari/537.36'}
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        with open(save_path, 'wb') as file:
            file.write(response.read())
        print(f"Image downloaded successfully and saved at {save_path}")
    except Exception as e:
        print(f"Failed to download image. Error: {e}")

# Example usage:
image_url = main()
save_path = 'C:\\Users\\FloMo\\Downloads\\py\\downloaded_image.png'
download_image(image_url, save_path)

#print(main())
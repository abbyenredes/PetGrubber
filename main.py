import requests
from bs4 import BeautifulSoup as bs
import random
import time
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# configuracion de navegador
def main():
    browser = uc.Chrome()
    url = 'https://www.tiendanimal.es/home-friends-heno-de-manzanilla-para-roedores/HOMCOM308050_M.html'
    browser.get(url)
    browser.implicitly_wait(10)
    # automatizacion para aceptar cookies
    cookie_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
    cookie_button.click()
    html = browser.page_source
    soup = bs(html, 'lxml')
    soup
    # browser.close() # cerrar pestaña
    input("Presiona Enter para cerrar el navegador...")
    browser.quit() # cerrar navegador
    
    # extraccion de datos
    product_name = soup.find('h1', class_='product-page-title-block__title').text
    print(product_name)

    product_brand = soup.find('a', class_='isk-link is-small product-page-title-block__brand').text
    print(product_brand)
    
    product_price = soup.find('span', class_='product-page-action__price').text
    print(product_price)
    
    product_rating = soup.find('div', class_='product-page-title-block__rating').text
    print(product_rating)
    

if __name__ == '__main__':
    main()
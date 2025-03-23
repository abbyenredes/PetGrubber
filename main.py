from py_compile import main
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_product(url):
    # Configuración del navegador
    browser = uc.Chrome()
    url = 'https://www.tiendanimal.es/flamingo-sticks-de-madera-para-roer-/FLA7370_M.html'
    browser.get(url)
    
    try:
        # Aceptar cookies de forma automatizada
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
        ).click()
    except Exception as e:
        print("No se encontró botón de cookies o ya estaba aceptado.")
    
    # Parcear el HTML
    html = browser.page_source
    soup = bs(html, 'lxml')
    

    browser.quit() # Cerrar el navegador
    
    # extraccion de datos
    product_name = soup.find('h1', class_='product-page-title-block__title').text
    print(product_name)

    product_price = soup.find('span', class_='product-page-action__price').text
    print(product_price)
    
    product_description = soup.find('div', class_='product-page-details__content is-long').text
    print(product_description)
    
    product_rating = soup.find('div', class_='product-page-title-block__rating').text
    print(product_rating)
    
    ''''
    product_stars = soup.find('div', class_='product-page-title-block__stars').text
    print(product_stars)
    '''


if __name__ == '__main__':
    main()

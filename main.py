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
    
    # Extraer datos con manejo de errores
    try:
        product_name = soup.find('h1', class_='product-page-title-block__title').text.strip()
    except:
        product_name = 'No disponible'
    
    try:
        product_brand = soup.find('a', class_='isk-link is-small product-page-title-block__brand').text.strip()
    except:
        product_brand = 'No disponible'
    
    try:
        product_price = soup.find('span', class_='product-page-action__price').text.strip()
        product_price = product_price.replace('€', '').replace(',', '.').strip()
    except:
        product_price = 'No disponible'
    
    try:
        product_rating = soup.find('div', class_='product-page-title-block__rating').text.strip()
    except:
        product_rating = 'No disponible'
    
    return {
        'Nombre': product_name,
        'Marca': product_brand,
        'Precio (€)': product_price,
        'Valoración': product_rating
    }

def main():
    url = 'https://www.tiendanimal.es/jr-farm-pelota-de-sause-con-heno-para-roedores/JRFJR07709_M.html'
    data = scrape_product(url)
    
    # Guardar datos en un DataFrame de Pandas con formato limpio
    df = pd.DataFrame([data])
    df.to_csv('productos.csv', index=False, sep=';', encoding='utf-8')
    print("Datos guardados en productos.csv con exito!")

if __name__ == '__main__':
    main()

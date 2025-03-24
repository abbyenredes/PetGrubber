# PetGrubber
El webscrapper que todo amante de los animales debe conocer 🦴
 ## Acerca del proyecto:
 
 ¿Cansado de pasar horas buscando los mejores productos para tu mascota?

 Esta herramienta es para ti, optimiza esa busqueda con un solo click, enseñandote los productos con mejor valoración y permitiendote elegir lo mejor para tu compañero peludo. 
 
## Mis recursos
* Tienda demo para practicar selenium: [saucedemo](https://www.saucedemo.com/)
* Libreria demo para practicar webscraping:  [books.toscrape](https://books.toscrape.com/)
* Video del que saque la logica de selenium: [Webscrapping idealista](https://www.youtube.com/watch?v=JKwfzexrQS0&ab_channel=JaviDataScience)
* Tutorial de pandas: [pandas](https://www.datacamp.com/es/tutorial/pandas)
* Guia sobre webscrepping: [La guía definitiva para Web Scraping](https://www.rapidseedbox.com/es/blog/web-scraping)

## Como usar PetGrubber
> [!WARNING]
> este programa esta creado con la version de python3.10

### 🚀 Instalación y Configuración

### 1️⃣ Clonar el repositorio y entrar

```textplain
git clone https://github.com/tu-API
cd tu-API
```

### 2️⃣ Descarga el entorno virtual:
⚠️ linux/mac
```textplain
python3.10 -m venv .venvv
```
⚠️ windows
```texrplain
python3.10 -m venv .venv
```

### 3️⃣ Inicia el entorno virtual:
⚠️ linux/mac
```textplain
source .venv/bin/activate
```
⚠️ windows
```textplain
.venv\Scripts\activate
```

### 4️⃣ Descarga las siguientes dependencias:
```textplain
 pip install -r requirements.txt
```

> [!TIP]
> Con `pip list` puedes visualizar todas las dependencias descargadas.

### 5️⃣ Ejecuta el scrapper 

```textplain
python3 main.py
```

### Disfruta del resultado

![video_demo]()

### Mi paso a paso

1️⃣ ¿Cual es mi finalidad?

Primero pense en que datos gustaría scrappear, me gusta el mundo de los animales así que me parecio una gran oportunidad aportar valor y una de mis metas fue [tiendanimal](https://www.tiendanimal.es/), visualice su [robots.txt](https://www.tiendanimal.es/robots.txt) y me di cuenta que todo en su **User-agent** estaba en **Disallow** lo que significa que esta página no desea ser scrappeada. Son pocas las páginas que realmente lo permitan pero eso no me freno a continuar.

2️⃣ Definiendo los datos:
Según mi experiencia como asistente veterinario y tutora de mascotas, los datos revelantes para extraer en esta tienda son:

* Nombre del producto
* Marca
* Precio
* Calificación (este para mi es un dato muy importante, quiero darle calidad de vida a mis mascotas sin importar si es mas costoso)

3️⃣ Examinar donde estan esos datos y para ello use la opcion de inspeccionar página.

![video-inspeccionar]()

4️⃣ Definir que biblioteca de websrappping usar.

| Librería        | Descripción | Pros | Contras |
|----------------|------------|------|---------|
| **BeautifulSoup** | Analiza y extrae datos de HTML y XML de forma sencilla. | ✅ Fácil de usar, flexible, ideal para proyectos pequeños y medianos. | ❌ No descarga páginas web, necesita `requests` o `urllib`. Lento para grandes volúmenes de datos. |
| **Scrapy**      | Framework completo para web scraping, permite rastrear y extraer datos de múltiples páginas de manera eficiente. | ✅ Rápido, eficiente, maneja peticiones asíncronas, tiene soporte integrado para middlewares y almacenamiento de datos. | ❌ Curva de aprendizaje más alta, puede ser excesivo para tareas simples. |
| **Requests**    | Librería para hacer peticiones HTTP de manera sencilla y obtener el HTML de las páginas web. | ✅ Fácil de usar, permite manejar sesiones y autenticaciones. | ❌ No parsea HTML ni interactúa con JavaScript. Se usa junto con BeautifulSoup o lxml. |
| **Selenium**    | Automación de navegadores, permite interactuar con páginas web dinámicas. | ✅ Soporta JavaScript y páginas dinámicas, permite interactuar con formularios y botones. | ❌ Lento en comparación con Scrapy, requiere un navegador instalado. |

En mi caso empece creando un script básico con  **BeautifulSoup**  **Requests** y me encontre mi primer problema, mi versión de python no era apta para **BeautifulSoup**

```shell
PetGrubber on  main [?] via 🐍 v3.13.0a3 (.venv) 
❯ python3 -c "from bs4 import BeautifulSoup; print(BeautifulSoup('<html></html>', 'html.parser'))"
Segmentation fault (core dumped)
```
Después de investigar y probar que habia descargado correctamente, borrar y volver a crear mi entorno visual di que era por mi version de python. Mi solucion:

Borrar nuevamente mi entorno virtual:
```textplain
rm -rf .venv
```
instalarlo con python3.10
```textplain
python3.10 -m venv .venv
```
Descargar mis dependencias
```textplain
pip install beautifulsoup4 lxml requests
```
✔️ probar lo que llevaba de script

¿Por qué con esta versión y no con otra?
pues probe desde 3.12, 3.11 y solo con la 3.10 funciono.

```shell
PetGrubber on  main [?] via 🐍 v3.13.0a3 (.venv) 
❯ python3.12 -c "from bs4 import BeautifulSoup; print(BeautifulSoup('<html></html>', 'html.parser'))"
Command 'python3.12' not found, did you mean:
  command 'python3.10' from deb python3.10 (3.10.12-1~22.04.9)
  command 'python3.11' from deb python3.11 (3.11.0~rc1-1~22.04)
Try: sudo apt install <deb name>
```
Con esta version **BeautifulSoup** es estable y compatible

```shell
PetGrubber on  main [?] via 🐍 v3.13.0a3 (.venv) 
❯ python3.10 -c "from bs4 import BeautifulSoup; print(BeautifulSoup('<html></html>', 'html.parser'))"
<html></html>
```
Pactique un poco con esta página: [books.toscrape](https://books.toscrape.com/) ya que no queria ser baneada por parecer un bot. En esta mi misión era aprender a hacer scrapping por puntuacion y solo descargar los libros con la mejor puntuación, esta es mi práctica:

```python
import bs4
import requests

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# iterar paginas
for pagina in range(1, 51):

    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    for libro in libros:

        # chequear que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            titulo_libro = libro.select('a')[1]['title']
            titulos_rating_alto.append(titulo_libro)

# ver libros 4 u 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)
```

Con esta base implemnte mi primera versión pero me tope con varios inconvenientes que me hicieron elegir usar **Selenium** y el primero fue el manejo de cookies y una implementación  para no ser baneado facilmente de las páginas.

5️⃣ Guardado de esos datos

Al principio necesitaba ver que los datos extraidos eran los correctos y use la función `printf`, sin embargo eso no es lo óptimo probe con json pero la verdad esteticamente no me gusto y por ello elegí Pandas ya que me exporta los datos en un documento cvs de una forma dinamica.
aqui dejo un resumen de sus distintos módulos:

| Método               | Descripción                                                                                      | Ejemplo                                                                                           |
|----------------------|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| `read_csv()`         | Importa datos desde un archivo CSV a un DataFrame.                                               | `df = pd.read_csv('datos.csv')`                                                                   |
| `head()`             | Muestra las primeras n filas del DataFrame (por defecto, n=5).                                   | `df.head()`                                                                                       |
| `tail()`             | Muestra las últimas n filas del DataFrame (por defecto, n=5).                                    | `df.tail()`                                                                                       |
| `info()`             | Proporciona un resumen conciso del DataFrame, incluyendo el número de entradas y tipos de datos. | `df.info()`                                                                                       |
| `describe()`         | Genera estadísticas descriptivas para las columnas numéricas del DataFrame.                      | `df.describe()`                                                                                   |
| `sort_values()`      | Ordena el DataFrame según los valores de una o más columnas.                                     | `df.sort_values(by='columna', ascending=True)`                                                    |
| `groupby()`          | Agrupa el DataFrame utilizando una o más columnas y permite aplicar funciones de agregación.     | `df.groupby('columna').mean()`                                                                    |
| `drop_duplicates()`  | Elimina filas duplicadas del DataFrame.                                                          | `df.drop_duplicates()`                                                                            |
| `rename()`           | Cambia el nombre de las columnas o filas del DataFrame.                                          | `df.rename(columns={'viejo_nombre': 'nuevo_nombre'})`                                             |
| `value_counts()`     | Cuenta la cantidad de ocurrencias únicas de valores en una serie o columna.                      | `df['columna'].value_counts()`                                                                    |
| `merge()`            | Combina dos DataFrames basándose en una clave común.                                             | `pd.merge(df1, df2, on='columna_clave')`                                                          |
| `pivot_table()`      | Crea una tabla dinámica que resume los datos según las variables especificadas.                  | `df.pivot_table(values='columna_valor', index='columna_indice', columns='columna_columnas')`      |
| `fillna()`           | Rellena los valores NaN (nulos) con un valor específico.                                         | `df.fillna(valor=0)`                                                                              |
| `dropna()`           | Elimina las filas o columnas que contienen valores nulos.                                        | `df.dropna()`                                                                                     |
| `apply()`            | Aplica una función a lo largo de un eje del DataFrame (filas o columnas).                        | `df['columna'].apply(funcion)`                                                                    |
| `astype()`           | Convierte el tipo de datos de una o más columnas.                                                | `df['columna'] = df['columna'].astype(int)`                                                       |
| `set_index()`        | Establece una columna específica como el índice del DataFrame.                                   | `df.set_index('columna')`                                                                         |
| `reset_index()`      | Restablece el índice del DataFrame al valor predeterminado.                                      | `df.reset_index()`                                                                                |
| `loc[]`              | Accede a un grupo de filas y columnas por etiquetas o una matriz booleana.                       | `df.loc[filas, columnas]`                                                                         |
| `iloc[]`             | Accede a un grupo de filas y columnas por índices enteros.                                       | `df.iloc[filas, columnas]`                                                                        |


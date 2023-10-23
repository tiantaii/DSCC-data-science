import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

url = 'https://www.bfs.admin.ch/bfs/en/home/services/recherche/experimental-statistics.html.'
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # Encuentra todos los enlaces en la página
    enlaces = soup.find_all('a')

    # Nombre del archivo CSV donde guardarás los enlaces
    nombre_archivo = 'enlaces.csv'

    # Abre el archivo CSV en modo escritura
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        # Crea un objeto escritor CSV
        csv_writer = csv.writer(archivo_csv)

        # Escribe una fila de encabezado (opcional)
        csv_writer.writerow(['Texto del enlace', 'URL del enlace'])

        # Escribe los enlaces en el archivo CSV
        for enlace in enlaces:
            texto_enlace = enlace.text
            url_enlace = enlace.get('href')
            csv_writer.writerow([texto_enlace, url_enlace])

    print(f'Los enlaces se han guardado en {nombre_archivo}')
else:
    print(f'Error al cargar la página: {response.status_code}')

    data = {'Categoría': ['A', 'B', 'C', 'D'],
        'Cantidad': [10, 15, 8, 12]}
df = pd.DataFrame(data)
plt.bar(df['Categoría'], df['Cantidad'])
plt.xlabel('Categoría')
plt.ylabel('Cantidad')
plt.title('Gráfico de Barras')
plt.show()

# Gráfico de Dispersión (Scatter Plot)
x = np.random.rand(50)  # Datos en el eje X
y = np.random.rand(50)  # Datos en el eje Y
plt.scatter(x, y)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de Dispersión')
plt.show()

# Gráfico de Línea (Line Chart)
data = {'Año': [2010, 2011, 2012, 2013, 2014],
        'Ventas': [100, 120, 90, 110, 130]}
df = pd.DataFrame(data)
plt.plot(df['Año'], df['Ventas'])
plt.xlabel('Año')
plt.ylabel('Ventas')
plt.title('Gráfico de Línea')
plt.grid(True)
plt.show()
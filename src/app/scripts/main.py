import pandas as pd
import requests
from io import BytesIO

# URL RAW del archivo Excel en GitHub
url = 'https://raw.githubusercontent.com/apocalipto77/Bigdata_2025_1_2/main/Indice%20de%20accidentes.xlsx'

# Descargar el archivo desde GitHub
response = requests.get(url)
response.raise_for_status()  # Verifica que la descarga fue exitosa

# Leer el archivo Excel desde la memoria
df = pd.read_excel(BytesIO(response.content))

# Mostrar las primeras filas para verificar
print(df.head())



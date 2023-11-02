import pandas as pd
from typing import Set
import requests


def ej_1_cargar_datos_demograficos() -> pd.DataFrame:
    url = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
    data = pd.read_csv(url, sep=';')
    data = data[['City', 'State', 'Median Age', 'Male Population', 'Female Population','Total Population', 'Foreign-born','Average Household Size', 'State Code']]
    data.drop_duplicates(subset=['City'],keep='first')
    return data

def ej_2_cargar_calidad_aire(ciudades: Set[str]) -> None:
    df = pd.DataFrame(columns=['ciudad','CO', 'NO2', 'O3', 'SO2', 'PM2.5', 'PM10', 'overall_aqi'])
    for ciudad in ciudades :
        api_url = f'https://api.api-ninjas.com/v1/airquality?city={ciudad}'
        response = requests.get(api_url, headers={'X-Api-Key': 'z4n1O92Br9WBOUNiW5E4Tg==HIVzphiQDwourmIV'})
        if response.status_code == requests.codes.ok:
            datos = response.json()
            row = [ciudad, datos['CO']["concentration"], datos['NO2']["concentration"], datos['O3']["concentration"], datos['SO2']["concentration"], datos['PM2.5']["concentration"], datos['PM10']["concentration"], datos['overall_aqi']]
            df.loc[len(df)] = row
    pass
import pandas as pd


def diff_cities(df):
    different_cities = df[df['municipio_paciente']!= df['municipio_atendimento']]
    different_cities.to_csv('data/02_processed/different_cities.csv', index=False)
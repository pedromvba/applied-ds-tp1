import streamlit as st
from dotenv import load_dotenv
import os
import json
import requests
import pandas as pd
import altair as alt
import time
from services.functions import *
from services.plots import *


@st.cache_data
def read_data(file_path):
    return pd.read_csv(file_path)

# importing environment variables and creating others
load_dotenv()
FILE_PATH_DIFF = 'data/02_processed/different_cities.csv'
FILE_PATH_FULL= 'data/02_processed/full_data.csv'
gmaps_key = os.getenv('GMAPS_API_KEY')

# loading data
diff_cities = read_data(FILE_PATH_DIFF)
full_data = read_data(FILE_PATH_FULL)




# page
st.header('Direcionador de Investimento')
st.write('''
         
Nesta aba do aplicativo, temos como objetivo realizar a análise dos 
dados e obter insights sobre oportunidades de investimentos que possam tanto subsidiar
gestores da saúde na melhor alocação de recursos públicos, bem como evidenciar ao setor privado
oportunidades de investimento que possam trazer retornos.

Sobre o tema, a aba propõe identificar as principais localidades e procedimentos para os quais os 
cidadãos tem que se deslocar até outra localidade para serem atendidos.

    '''

)

st.write('## Atendimentos realizados fora do Município do Cidadão')

col1,col2 = st.columns(2)

col1.write('### Número de Cidadãos que se deslocaram buscando atendimento:')

trip_count = diff_cities['municipio_paciente'].value_counts().reset_index()
trip_count.columns = ['Município', 'Contagem de Deslocamentos']

col1.dataframe(trip_count)


col2.write('### Número de Atendimentos realizados em cidadãos de outros Municípios:')

care_count = full_data['municipio_atendimento'].value_counts().reset_index()
care_count.columns = ['Município', 'Contagem de Atendimentos']

col2.dataframe(care_count)


# merging data to plot
combined_data = pd.merge(trip_count, care_count, on='Município', how='outer').fillna(0)

# scatterplot
st.write('### Deslocamentos vs. Atendimentos por Município')
st.write('''

A partir do gráfico abaixo é possível evidenciar as categorias dos municípios. 

* Categoria 1: Municípios com
uma melhor infraestrutura hospitalar, para o qual seus cidadãos, como regra, não precisam se deslocar
para receber um atendimento adequado.
         
            Valores altos de contagem de atendimentos e baixos de contagem de deslocamento
         
* Categoria 2: Municípios com infraestrutura hospitalar mais limitada e para os quais ocorre deslocamento
para outros municípios.

            Valores baixos de contagem de atendimentos e altos de contagem de deslocamento 

'''
)

# scatter plot
scatter_trip_care_count(combined_data)

############################### TRABALHANDO ###################################

st.write('## Métricas de Deslocamento e Tempo de Viagem Anuais')


st.write('''
Nesta seção, busca-se evidenciar e concretizar em métricas 
como distância e tempo de deslocamento, o esforço empregado pelo cidadão para ser atendido pelo SUS.
         '''
)




###########################################################################################
st.write('## Análise do Deslocamento do Cidadão')



col1, col2 = st.columns(2)
origin = col1.selectbox(
    label = 'Selecione a cidade de origem do cidadão',
    options=diff_cities['municipio_paciente'].unique()
)

destination = col2.selectbox(
    label = 'Selecione a cidade de destino do cidadão',
    options=diff_cities['municipio_atendimento'].unique()
)


routes(origin, destination, gmaps_key)




# enriching data with distance and travel time

# creating city tuples
pairs = city_tuples(diff_cities)

# merging distance and time into diff_cities 

distance_time = []

for origin_city, destination_city in pairs:
    duration, distance = get_travel_time(gmaps_key, origin_city, destination_city)
    
    distance_time.append({
        'origin_city': origin_city,
        'destination_city': destination_city,
        'travel_time': duration,
        'distance': distance
    })

distance_time_df = pd.DataFrame(distance_time)

# merging data
merged_df = merging_distance_time(diff_cities, distance_time_df)


st.write(merged_df)


# colocar umas métricas também




anual_distance = merged_df.groupby('ano').sum()['distance'].reset_index()
anual_travel_time = merged_df.groupby('ano').sum()['travel_time'].reset_index()

st.write(anual_distance)
st.write(anual_travel_time)

col1,col2 = st.columns(2)

for year in anual_distance['ano'].unique():
    distance = (anual_distance.loc[anual_distance['ano'] == year, 'distance'].values[0])
    col1.metric( 
        label=f'Distância Percorrida Acumulada em {year} (bilhões de Km)', 
        value=f'{(distance/10E9):,.2f}'
    )

for year in anual_travel_time['ano'].unique():
    travel_time = (anual_travel_time.loc[anual_travel_time['ano'] == year, 'travel_time'].values[0])
    col2.metric( 
        label=f'Tempo de Viagem Acumulado {year} (dias)', 
        value=f'{(travel_time/(3600*24)):,.2f}'
    )    
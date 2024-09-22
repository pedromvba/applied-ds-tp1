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


# calculating trip and care counts
trip_count = diff_cities['municipio_paciente'].value_counts().reset_index()
trip_count.columns = ['Município', 'Contagem de Deslocamentos']

care_count = full_data['municipio_atendimento'].value_counts().reset_index()
care_count.columns = ['Município', 'Contagem de Atendimentos']


# page
st.header('Melhor Atendimento Mais Próximo')
st.write('''
         
Nesta aba do aplicativo, temos como objetivo direcionar o cidadão para o Município com melhor infraestrutura
de saúde mais próximo dele. Partimos do pressuposto que Municípios que realizam muitos atendimentos pelo SUS
possuem uma infraestrutura de saúde mais robusta do que os que realizam poucos.
         
Assim, elencamos os Municípios preferíveis para que o cidadão seja atendido com base nesse histórico e 
na raio de distância que o usuário informar.

Após a indicação do melhor Município para atendimento, a rota será traçada  automaticamente pelo google maps
    '''

)


st.write('## Indicando Cidade com Melhor Atendimento Mais Próxima')

origin = st.text_input(
    label = 'Insira o nome da sua localidade dentro do Estado de Roraima',
)

radius = st.number_input(
    label = 'Insira a distância máxima que deseja percorrer em quilômetros',
)

if origin and radius != 0:

    try:
        found_city = False

        city_options = care_count['Município'].unique()
        for city in city_options:
            destination = city
            duration, distance = get_travel_time(gmaps_key, origin, destination)
            if int(distance)/1000<= radius:
                care_city = city
                found_city = True
                st.write(f' A cidade com o melhor atendimento é: {care_city}')
                st.write(f' O tempo de viagem calculado é de: {convert_to_hours_minutes(duration)}')
                
                st.write('#### Rota Traçada')
                routes(origin, care_city, gmaps_key)
                st.write(care_city) 

                break
        
        if not found_city:
            st.write('Cidade não encotrada, favor aumentar o raio.')
        
        
    
    except:
        st.write('Localidade de Origem não identificada, favor inserir o nome do Município como ponto de Origem')




        






# col1, col2 = st.columns(2)
# origin = col1.selectbox(
#     label = 'Selecione a cidade de origem do cidadão',
#     options=diff_cities['municipio_paciente'].unique()
# )

# destination = col2.selectbox(
#     label = 'Selecione a cidade de destino do cidadão',
#     options=diff_cities['municipio_atendimento'].unique()
# )


# routes(origin, destination, gmaps_key)

#routes(origin, destination, gmaps_key)




# # scatterplot
# st.write('### Deslocamentos vs. Atendimentos por Município')
# st.write('''

# A partir do gráfico abaixo é possível evidenciar as categorias dos municípios. 

# * Categoria 1: Municípios com
# uma melhor infraestrutura hospitalar, para o qual seus cidadãos, como regra, não precisam se deslocar
# para receber um atendimento adequado.
         
#             Valores altos de contagem de atendimentos e baixos de contagem de deslocamento
         
# * Categoria 2: Municípios com infraestrutura hospitalar mais limitada e para os quais ocorre deslocamento
# para outros municípios.

#             Valores baixos de contagem de atendimentos e altos de contagem de deslocamento 

# '''
# )

# # merging data to plot
# combined_data = pd.merge(trip_count, care_count, on='Município', how='outer').fillna(0)
# # scatter
# scatter_trip_care_count(combined_data)
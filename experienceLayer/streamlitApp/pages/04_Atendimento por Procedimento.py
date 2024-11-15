import streamlit as st
import requests
import pandas as pd 



def localidades(procedimento):
    full_data = pd.read_csv('./data/02_processed/full_data.csv')
    localidades = full_data[full_data['procedimento_principal'] == procedimento]['municipio_atendimento']
    localidades = localidades.unique()
    localidades = pd.Series(localidades, name='municipio')

    return localidades

#st.dataframe(localidades("DIAGNOSTICO E/OU ATENDIMENTO DE URGENCIA EM CLINICA MEDICA"))


st.write('## Indicando Localidades com Atendimento Para a Especialidade Procurada')


st.write('### DESCRICAO')

if prompt:= st.chat_input('Que tipo de tratamento você precisa?'):
    with st.chat_message("user",avatar='👤'):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar='🤖'):
        with st.spinner("Estou pensando"):

            req = requests.post(
                url = 'http://localhost:8000/procedimento/',
                json = {'message': prompt})
            response = req.json()

            if response["assistant"] == "DIAGNOSTICO E/OU ATENDIMENTO DE URGENCIA EM CLINICA MEDICA":
                st.write("""Não conseguimos identificar um procedimento para sua solicitação, favor 
                         procurar um atendimento de urgência em uma das seguintes localidades:""")
                
                st.dataframe(localidades("DIAGNOSTICO E/OU ATENDIMENTO DE URGENCIA EM CLINICA MEDICA"))

            else:
                st.write(f"""Identificamos atendimento para o tratamento desejado nas seguintes localidades:""")
            
                st.dataframe(localidades(response["assistant"]))


            #st.write(response["assistant"])
            # atendimento para diabetes
            # acho que tenho malária
            # parto
            # tratamento para pneumonia
        
            
    


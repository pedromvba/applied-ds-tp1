import streamlit as st
import pandas as pd


app_name = 'Monitor da Saúde'

# Project Cover

# Basic Information
st.title(f'{app_name}')

st.subheader(f'Bem vindo ao {app_name}! 🏥')

st.image('images/Capa2.jpg')

st.write(f'''O projeto {app_name} tem como objetivo identificar municípios com potencial 
         de investimento em infraestrutura de saúde, baseado, tanto no deslocamento dos cidadãos 
         em busca de atendimento do SUS quanto nos procedimentos realizados em cada localidade.''')

st.write('''
O sistema de saúde público no Brasil é bastante abrangente, tanto em termos de procedimentos que podem 
ser realizados gratuitamente quanto no espaço geográfico que ele deve cobrir, considerando as dimensões do Brasil. 
Ao mesmo tempo, devido a essas características, bem como a definição na Constituição Nacional de que a saúde é
direito do cidadão, o sistema de saúde brasileiro necessita de um bom planejamento de investimentos. Nesse sentido, 
é importe que os gestores da saúde consigam ter uma visão resumida dos atendimentos realizados, bem como dos investimentos 
despendidos, de forma a planejar as despesas nos anos posteriores.

Além disso, uma das realidades que acomete o povo brasileiro é a infraestrutura de saúde mais 
simples longe das capitais, fazendo com que o público tenha que se deslocar grandes distâncias 
para ser atendido nas capitais. 

Assim, de forma a subsidiar o planejamento de gestores dos Ministério da Saúde para o ano posterior, 
bem como indicar localidades nas quais há espaço para incremento/investimento em infraestrutura de 
saúde, o aplicativo criado apresenta de forma compreensível e prática tais informações para que sejam 
utilizada por Prefeituras, parlamentares/candidatos, ONGs e Empresários do Setor da Saúde 
no suporte das justificativas das busca de seus objetivos, sejam eles votos, recursos financeiros, etc.
''')

# Usefull Links
st.subheader('Links Úteis')

st.write('''

[Github do Projeto](https://github.com/pedromvba/applied-ds-tp1)

[Dados do Projeto](https://drive.google.com/file/d/1sNKzhx4-ATKZ2tqLI8mPeVx1YYeMMoiv/view?usp=share_link).
         
[Inspiração para o Projeto - Medium](https://medium.com/data-hackers/explorando-dados-do-sus-com-sql-e9c6cfc08cc2)

Contato do Desenvolvedor: pedromvba@gmail.com         
         
''')

# Data Sample
df = pd.read_csv('./data/02_processed/processed_data.csv')

st.subheader('Amostra dos Dados')
st.dataframe(df.head(10))

# Data Dictionary
st.subheader('Dicionário dos Dados')
st.write('''

         
Quantidade de Procedimentos: quantidade de procedimentos realizados no atendimento

Mês: mês de realização do atendimento

Ano: ano de realização do atendimento

Sigla UF : Estado no qual foi realizado o atendimento

Valor Ato Profissional: valor do procedimento realizado

Município Paciente: Município de domicílio do paciente

Município Atendimento: Município no qual o paciente foi atendido

Procedimento Principal: principal atendimento realizado
         

         

''')

import streamlit as st

# applying the backgroud color saved in the session state
background_color = st.session_state['backgroud_state']

st.markdown(
    f'''
    <style>
    [data-testid="stApp"] {{
        background-color: {background_color}
    }}
    </style>
    ''',
    unsafe_allow_html=True)

st.header ('Modelo de Regressão Linear')

st.write('Em desenvolvimento')
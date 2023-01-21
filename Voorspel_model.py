import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from statistics import median

st.set_page_config(layout="wide", page_title='Dashboard Overheating houses', initial_sidebar_state='expanded')
# data_main = pd.read_excel('SimulatieInvoerEnComfortResult_v2.xlsx', sheet_name='compleet')
data_main = pd.read_csv('Streamlit Data.csv')

data_A = data_main.copy()
data_B = data_main.copy()


def left_align(s, props='text-align: left;'):
    return props
description = pd.DataFrame({'Eigenschap':['Glaspercentage', 'g-waarde glas', 'Isolatie/Infiltratie', 'Oriëntatie', 'Spuiventilatie', 'Klimaatbestand', 'Zonwering', 'Woningtype'], 
'Beschrijving':['Glaspercentage geeft aan wat het percentage van de wanden uit glas bestaat.', 
'g-waarde glas is een karakteristiek van glas dat aangeeft hoeveel energie van de zon wordt doorgelaten.',
'Isolatie/Infiltratie geeft de kwaliteit van uw isolatie/infiltratie aan', 
'Oriëntatie is de richting waarop het huis staat.',
"Spuiventilatie geeft de manier van het huis ventileren aan. Hier zijn de keuzes overdag ventileren, 's nachts ventileren of volgens de TO-juli standaard ventileren.",
'Klimaatbestand geeft de plaatsing van het huis aan. Hierin is 1 het platteland, 2 de stad en 3 het platteland 10 jaar in de toekomst.',
'Zonwering beschrijft hoe het huis tegen de zon wordt beschermd.',
'Woningtype geeft het type woning aan waar u in woont']}).set_index('Eigenschap')
description.columns.name = description.index.name
description.index.name = None


col1, col2 = st.columns([1,1])
with col1:
    with st.form(key='my_form'):
        commit = st.form_submit_button('Submit')
        Glaspercentage1 = st.selectbox('Selecteer Glaspercentage', ['Weet ik niet'] + list(data_main['Glaspercentage'].unique()))
        if Glaspercentage1 == 'Weet ik niet':
            data_A = data_A
        else:
            data_A = data_A[data_A['Glaspercentage']== Glaspercentage1]

        Isolatie_infiltratie1 = st.selectbox('Selecteer Isolatie/infiltratie', ['Weet ik niet'] + list(data_main['Isolatie/infiltratie'].unique()))
        if Isolatie_infiltratie1 == 'Weet ik niet':
            data_A = data_A
        else:
            data_A = data_A[data_A['Isolatie/infiltratie']== Isolatie_infiltratie1]

        g_waarde1 = st.selectbox('Selecteer g-waarde', ['Weet ik niet'] + list(data_main['g-waarde glas'].unique()))
        if g_waarde1 == 'Weet ik niet':
            data_A = data_A
        else:
            data_A = data_A[data_A['g-waarde glas']== g_waarde1]

        Spuiventilatie1 = st.selectbox('Selecteer Spuiventilatie', ['Weet ik niet'] + list(data_main['Spuiventilatie'].unique()))
        if Spuiventilatie1 == 'Weet ik niet':
            data_A = data_A
        else:
            data_A = data_A[data_A['Spuiventilatie']== Spuiventilatie1]

        Zonwering1 = st.selectbox('Selecteer Zonwering', ['Weet ik niet'] + list(data_main['Zonwering'].unique()))
        if Zonwering1 == 'Weet ik niet':
            data_A = data_A
        else:
            data_A = data_A[data_A['Zonwering']== Zonwering1]

        Oriëntatie1 = st.selectbox('Selecteer Oriëntatie', ['Weet ik niet'] + list(data_main['Oriëntatie'].unique()))
        if Oriëntatie1 == 'Weet ik niet':
            data_A = data_A
        else:
            data_A = data_A[data_A['Oriëntatie']== Oriëntatie1]

        Woningtype1 = st.selectbox('SelecteerWoningtype', ['Weet ik niet'] + list(data_main['Woningtype'].unique()))
        if Woningtype1 == 'Weet ik niet':
            data_A = data_A
        else:
            data_A = data_A[data_A['Woningtype']== Woningtype1]

        Klimaatbestand1 = st.selectbox('Selecteer Klimaatbestand', ['Weet ik niet'] + list(data_main['Klimaatbestand'].unique()))
        if Klimaatbestand1 == 'Weet ik niet':
            data_A = data_A
        else:
            data_A = data_A[data_A['Klimaatbestand']== Klimaatbestand1]
#         kamer1 = st.selectbox('Selecteer Kamer', ['Weet ik niet'] + list(data_main['Ruimtetype'].unique()))
#         if kamer1 == 'Weet ik niet':
#             data_A = data_A
#         else:
#             data_A = data_A[data_A['Ruimtetype']== kamer1]
        st.markdown('Minimale GTO uren: ' + str(data_A['GTO'].min()))
        st.markdown('Maximale GTO uren: ' + str(data_A['GTO'].max()))
        st.markdown('Verschil tussen min en max: ' + str(data_A['GTO'].max()-data_A['GTO'].min()))
        st.markdown('Mediaan: ' + str(median(data_A['GTO'])))

with col2:
    with st.form(key='my_form2'):
        commit = st.form_submit_button('Submit')
        Glaspercentage2 = st.selectbox('Selecteer Glaspercentage', ['Weet ik niet'] + list(data_main['Glaspercentage'].unique()), key=2)
        if Glaspercentage2 == 'Weet ik niet':
            data_B = data_B
        else:
            data_B = data_B[data_B['Glaspercentage']== Glaspercentage2]

        Isolatie_infiltratie2 = st.selectbox('Selecteer Isolatie/infiltratie', ['Weet ik niet'] + list(data_main['Isolatie/infiltratie'].unique()),key=3)
        if Isolatie_infiltratie2 == 'Weet ik niet':
            data_B = data_B
        else:
            data_B = data_B[data_B['Isolatie/infiltratie']== Isolatie_infiltratie2]

        g_waarde2 = st.selectbox('Selecteer g-waarde', ['Weet ik niet'] + list(data_main['g-waarde glas'].unique()), key=4)
        if g_waarde2 == 'Weet ik niet':
            data_B = data_B
        else:
            data_B = data_B[data_B['g-waarde glas']== g_waarde2]

        Spuiventilatie2 = st.selectbox('Selecteer Spuiventilatie', ['Weet ik niet'] + list(data_main['Spuiventilatie'].unique()), key=5)
        if Spuiventilatie2 == 'Weet ik niet':
            data_B = data_B
        else:
            data_B = data_B[data_B['Spuiventilatie']== Spuiventilatie2]

        Zonwering2 = st.selectbox('Selecteer Zonwering', ['Weet ik niet'] + list(data_main['Zonwering'].unique()), key=6)
        if Zonwering2 == 'Weet ik niet':
            data_B = data_B
        else:
            data_B = data_B[data_B['Zonwering']== Zonwering2]

        Oriëntatie2 = st.selectbox('Selecteer Oriëntatie', ['Weet ik niet'] + list(data_main['Oriëntatie'].unique()), key=7)
        if Oriëntatie2 == 'Weet ik niet':
            data_B = data_B
        else:
            data_B = data_B[data_B['Oriëntatie']== Oriëntatie2]

        Woningtype2 = st.selectbox('SelecteerWoningtype', ['Weet ik niet'] + list(data_main['Woningtype'].unique()), key=8)
        if Woningtype2 == 'Weet ik niet':
            data_B = data_B
        else:
            data_B = data_B[data_B['Woningtype']== Woningtype2]

        Klimaatbestand2 = st.selectbox('Selecteer Klimaatbestand', ['Weet ik niet'] + list(data_main['Klimaatbestand'].unique()), key=9)
        if Klimaatbestand2 == 'Weet ik niet':
            data_B = data_B
        else:
            data_B = data_B[data_B['Klimaatbestand']== Klimaatbestand2]
#         kamer2 = st.selectbox('Selecteer Kamer', ['Weet ik niet'] + list(data_main['Ruimtetype'].unique()), key=10)
#         if kamer2 == 'Weet ik niet':
#             data_A = data_A
#         else:
#             data_A = data_A[data_A['Ruimtetype']== kamer2]
        st.markdown('Minimale GTO uren: ' + str(data_B['GTO'].min()))
        st.markdown('Maximale GTO uren: ' + str(data_B['GTO'].max()))
        st.markdown('Verschil tussen min en max: ' + str(data_B['GTO'].max()-data_B['GTO'].min()))
        st.markdown('Mediaan: ' + str(median(data_B['GTO'])))

st.header("Parallel coördinaten plot")
st.markdown('''In een parallel coördinaten plot is het mogelijk om verschillende waardes van variabelen aan en uit te zetten. Dit doe je door op de waardes te klikken.
Dit laat een balk op die waarde komen, welke je kan uitrekken en inkorten om de selectie te vergroten of te verkleinen.''')
st.markdown('De kleur van de lijnen geeft de GTO uren aan, hoe roder de lijn hoe lager de GTO uren en hoe paarser de lijn hoe hoger de GTO uren.')
st.markdown('Hieronder een tabel met beschrijvingen van de verschillende eigenschappen')
st.write(description.style.applymap(left_align).to_html(), unsafe_allow_html=True)
HtmlFile = open("file.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height = 600)


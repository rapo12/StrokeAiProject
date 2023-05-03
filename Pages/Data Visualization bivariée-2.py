import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd


st.set_page_config(page_title='Projet Ai', page_icon=':bar_chart:', layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)

var=st.sidebar.selectbox("Select an option", ["BiVariables quantitatives", "BiVariables qualitatives","BiVariables qualitative quantitative"])
if var == "BiVariables quantitatives":
    ##Streamlit code:
    st.title("Analyse bivarariée entre deux variables quantitatives")
    st.write("Du plot de densités conditionnelles de variables quantitatives, on a remarqué que l'AVC depend fortement de l'age. Dans cette rebrique, on calcule la corrélation qui est entre les différentes variables quantitatives deux à deux: age, avg_glucose_level et bmi.")
    variable_x =st.sidebar.selectbox("Veuillez choisir deux variables quantitatives différentes:", ["age", "bmi","avg_glucose_level"])
    variable_y =st.sidebar.selectbox("Sélectionner la deuxième", ["age", "bmi","avg_glucose_level"])

elif var =="BiVariables qualitatives":
    ##Streamlit code:
    st.title("Analyse bivariée entre deux variables qualitatives")
    column_name=st.sidebar.selectbox("Veuillez parcourir les variables une par une", ["gender", "hypertension","heart_disease","ever_married","work_type","Residence_type","smoking_status","stroke"])
else:
    st.title("Représentation graphique de Variables quantitatives")

import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Projet Ai', page_icon=':bar_chart:', layout='wide')
data_balanced = pd.read_csv("data/data_balanced.csv")
def plot_distribution(variablename):
    #plt.figure(figsize=(8,6))
    plt.rcParams['figure.figsize'] = [5, 3]
    sns.countplot(y="stroke_c", hue=variablename, data=data_balanced)
    plt.title(variablename.title()+" distribution")
    plt.legend(loc="lower center")
    st.pyplot()
    print_statistic(variablename)
def print_statistic(variablename):
    summary_table = (data_balanced.groupby(variablename)
                     .agg(total=(variablename, 'count'),
                          percent=(variablename, lambda x: round(len(x) / len(data_balanced), 3)),
                          strokes=('stroke_c', lambda x: sum(x == "stroke")),
                          stroke_percent=('stroke_c', lambda x: round(sum(x == "stroke") / len(x), 3))).reset_index())
    st.table(summary_table)
    # st.write("seceond display")
    # st.dataframe(summary_table)

if st.sidebar.selectbox("Select an option", ["Analyse exploratoire", "Densités conditionnelles"]) == "Analyse exploratoire":
    ##Streamlit code:
    st.title("Analyse exploratoire des variables qualitatives")
    column_name = st.sidebar.selectbox(
        "Veuillez parcourir les variables une par une pour voir l'efféctif de chaque classe de la variable choisie:",
        ["gender", "hypertension", "heart_disease", "ever_married", "work_type", "Residence_type", "smoking_status",
         ])
    plot_distribution(column_name)


else:
    ##Streamlit code:
    st.title("Représentation graphique de variables qualitatives")
    variable = st.sidebar.selectbox(
        "Veuillez parcourir les variables une par une pour voir l'efféctif de chaque classe de la variable choisie:",
        ["age", "bmi", "avg_glucose_level"])
import streamlit as st
import pandas as pd
#import networkx as nx
#import plotly.graph_objects as go

from utils.data_processing import load_data_1
from utils.charts import generate_dashboard

st.set_page_config(page_title="Diagramme de Flux", page_icon="🔀", layout="wide")

st.title("Diagramme de Flux")




def main():
    st.title("Tableau de Bord des Performances")
    
    # Charger les données
    df_eff = load_data_1()
    
    # Sélectionner un collège et une classe
    college = st.selectbox("Choisir un collège", df_eff['college'].unique())
    classe = st.selectbox("Choisir une classe", df_eff[df_eff['college'] == college]['classe'].unique())
    
    # Filtrer les données par collège et classe
    df_college_classe = df_eff[(df_eff['college'] == college) & (df_eff['classe'] == classe)]
    
    # Générer le tableau de bord
    dashboard = generate_dashboard(df_college_classe)
    
    # Afficher le tableau de bord
    st.plotly_chart(dashboard)

if __name__ == "__main__":
    main()









st.markdown(':orange[Application web développée par : Chabi Zimé GOUNOU N\'GOBI, Planificateur, DataManager/DataScientist]:computer:')
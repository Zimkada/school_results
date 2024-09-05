import streamlit as st
import pandas as pd
#import networkx as nx
#import plotly.graph_objects as go

from utils.data_processing import load_data_eff, load_data_prcent, processing
from utils.charts import generate_dashboard 

st.set_page_config(page_title="Diagramme de Flux", page_icon="🔀", layout="wide")

st.title(":blue[Tableau de Bord des Performances]")


def main():
    
    
    # Charger les données
    df_1 = load_data_eff()
    df_2 = load_data_prcent()

    # Preparation des données 
    df_eff = processing(df_1)
    df_percent = processing(df_2)


    # Générer le tableau de bord
    dashboard = generate_dashboard(df_eff, df_percent)
    

    # Afficher le tableau de bord
    st.plotly_chart(dashboard)

if __name__ == "__main__":
    main()






st.markdown("""    
    <div style="text-align: center; margin-top: 30px;">
        <span style="color: blue; font-size: 16px;"> Application web développée par :</span>
    </div>
    <div style="text-align: center; margin-top: 5px;">
        <span style="color: blue; font-size: 16px;">💻 Chabi Zimé GOUNOU N'GOBI, Planificateur, Data Manager/Data Scientist 💻</span>
    </div> 
                """, unsafe_allow_html=True)
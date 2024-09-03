import streamlit as st
import pandas as pd
import io
from utils.data_processing import processing, load_data_eff,load_data_prcent

st.set_page_config(page_title="Visualisation", page_icon="📊", layout="wide")


def main():
    st.title(":blue[Statistiques des Résultats Scolaires]")
    
    # Charger les données
    df_1 = load_data_eff()
    df_2 = load_data_prcent()

    # Preparation des données
    df_eff = processing(df_1)
    df_percent = processing(df_2)

    

    # Sélectionner un collège
    college = st.selectbox(":blue[Choisir un collège]", df_eff['college'].unique())
    
    # Filtrer les données par collège
    df_eff_college = df_eff[df_eff['college'] == college]
    df_percent_college = df_percent[df_percent['college'] == college]

    # Ajout du symbole % aux colonnes en pourcentage
    cols_to_exclude = ['N°','college','promotion']
    cols_to_modify = [col for col in df_percent.columns if col not in cols_to_exclude]
    for col in cols_to_modify:
        df_percent_college[col] = df_percent_college[col].apply(lambda x: f"{x:.1f}%" if isinstance(x, (int, float)) else x)
        #df_percent_college[col] = df_percent_college[col].astype(str) +'%'

    st.subheader(":blue[Tableau en effectifs]")
    st.write(df_eff_college)
    
    # Possibilité de télécharger les données
    # Création du buffer en mémoire pour écrire le fichier Excel
    buffer = io.BytesIO()
    
    # Écrire le DataFrame dans le buffer
    df_eff_college.to_excel(buffer, index=False)

    # Placer le pointeur au début du buffer
    buffer.seek(0)

    # Utiliser le buffer dans le st.download_button
    st.download_button(label="Télécharger les données des résultats scolaires en effectifs",
                    data=buffer,
                    file_name=f"Statisques_Resultats_{college}.xlsx",
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


    st.subheader(":blue[Tableau en pourcentages (%)]")
    st.write(df_percent_college)
    
    # Création du buffer en mémoire pour écrire le fichier Excel
    buffer = io.BytesIO()
    
    # Écrire le DataFrame dans le buffer
    df_percent_college.to_excel(buffer, index=False)

    # Placer le pointeur au début du buffer
    buffer.seek(0)

    # Utiliser le buffer dans le st.download_button
    st.download_button(label="Télécharger les données des résultats scolaires en %",
                    data=buffer,
                    file_name=f"Statisques_Resultats_Pourcentage_{college}.xlsx",
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == "__main__":
    main()
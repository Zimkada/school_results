import streamlit as st

st.set_page_config(page_title = 'Resultats scolaires Alibori', 
                   page_icon = '📚', layout = 'wide', 
                   initial_sidebar_state = 'expanded')


st.sidebar.success(":orange[Sélectionnez une page ci-dessus]")

def main():
    st.title(":rainbow[Application d'Analyse des Résultats Scolaires de l'Alibori]")
    
    st.markdown("""
    ### :blue[Bienvenue sur l'application web d'analyse des résulats scolaires]
    Cette application permet d'analyser les performances scolaires des élèves en fin d'année. 
    Vous pouvez explorer les statistiques des effectifs et des pourcentages, ainsi que visualiser les données sous forme de tableaux de bord interactifs.

    ### :blue[Guide d'utilisation :]
    - **:blue[Page Statistiques]** : Permet de sélectionner un collège et d'afficher les tableaux avec les données utiles.
    - **:blue[Page Dashboard (Tableau de bord)]** : Permet de visualiser les graphiques interactifs pour un collège et une classe sélectionnés.
    
     <span style="color:blue">👈 **Pour commencer, sélectionnez une page dans le menu de gauche.**</span>
    
    <div style="text-align: center; margin-top: 30px;">
        <span style="color: orange; font-size: 16px;"> Application web développée par :</span>
    </div>
    <div style="text-align: center; margin-top: 5px;">
        <span style="color: orange; font-size: 16px;">💻 Chabi Zimé GOUNOU N'GOBI, Planificateur, Data Manager/Data Scientist 💻</span>
    </div> 
                """, unsafe_allow_html=True)



if __name__ == "__main__":
    main()
   
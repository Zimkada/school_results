import plotly.graph_objs as go
from plotly.subplots import make_subplots
import streamlit as st
import numpy as np


def generate_dashboard(df1, df2):

#df1 = df_eff
#df2 = df_percent
    
# Sélectionner un collège et une promotion
    college = st.selectbox(":blue[Choisir un collège]", df1['college'].unique())
    promotion = st.selectbox(":blue[Choisir une promotion]", df1[df1['college']==college]['promotion'].unique())
    

    df_filtered_1 = df1[(df1['college'] == college) & (df1['promotion'] == promotion)]
    df_filtered_2 = df2[(df1['college'] == college) & (df2['promotion'] == promotion)]

    if df_filtered_2.empty:
        print("Aucune donnée disponible pour ce collège et cette promotion.")
        return
    
    # Identification des colonnes 
    F_moy_max_min = ['forte moyenne F', 'faible moyenne F']
    M_moy_max_min = ['forte moyenne M', 'faible moyenne M']
    
    T_cols = ['[inf 7.5[_T', '[7.5 9[_T', '[9 10[_T', '[10_12[_T', '[sup 12[_T']
    F_cols = ['[inf 7.5[_F', '[7.5 9[_F', '[9 10[_F', '[10_12[_F', '[sup 12[_F']
    M_cols = ['[inf 7.5[_M', '[7.5 9[_M', '[9 10[_M', '[10_12[_M', '[sup 12[_M']
    
    T_bar_cols = ['[inf 7.5[_T', '[sup 10[_T', '[sup 12[_T', '[sup 14[_T', '[sup 16[_T']
    F_bar_cols = ['[inf 7.5[_F', '[sup 10[_F', '[sup 12[_F', '[sup 14[_F', '[sup 16[_F']
    M_bar_cols = ['[inf 7.5[_M', '[sup 10[_M', '[sup 12[_M', '[sup 14[_M', '[sup 16[_M']

     
     # Création du tableau avec 3 lignes et 3 colonnes

    fig = make_subplots(
        rows=3, cols=3,
        subplot_titles=[
            "Radar des moyennes (élèves garçons et filles)", 
            "Répartition des moyennes (élèves garçons et filles)",
            "Radar des moyennes (élèves filles)", 
            "Répartition des moyennes (élèves filles)",
            "Plus forte et plus faible moyennes (élèves filles)",
            "Radar des moyennes (élèves garçons)",
            "Répartition des moyennes (élèves garçons)",
            "Plus forte et plus faible moyennes (élèves garçons)"
        ],
        specs=[[{"type": "polar"}, {"type": "bar", "colspan": 2}, None],
               [{"type": "polar"}, {"type": "bar"}, {"type": "bar"}],
               [{"type": "polar"}, {"type": "bar"}, {"type": "bar"}]]
    )

    # Première ligne : Total (T) - Garçons et filles
    fig.add_trace(go.Scatterpolar(r=df_filtered_2[T_cols].values[0], theta=[x[0:-2] for x in T_cols], fill='toself',
                                  text=[f"{np.round(val,1)}%" for val in df_filtered_2[T_cols].values[0]],
                                  marker=dict(size=10), name = "Radar (G et F)", hoverinfo="theta+text"), 
                                  row=1, col=1)
    
    fig.add_trace(go.Bar(x=T_bar_cols, y=df_filtered_2[T_bar_cols].values[0],
                         text=[f"{np.round(val,1)}%" for val in df_filtered_2[T_bar_cols].values[0]], 
                         textposition='auto', name = "Barres (G et F)", hoverinfo="x+text"), row=1, col=2)

    # Deuxième ligne : Filles (F) - Élèves uniquement
    fig.add_trace(go.Scatterpolar(r=df_filtered_2[F_cols].values[0], theta=[x[0:-2] for x in F_cols], fill='toself',
                                  text=[f"{np.round(val,1)}%" for val in df_filtered_2[F_cols].values[0]],
                                  marker=dict(size=10), name = "Radar (F)", hoverinfo="theta+text" ), 
                                  row=2, col=1)
    
    fig.add_trace(go.Bar(x=F_bar_cols, y=df_filtered_2[F_bar_cols].values[0],
                        text=[f"{np.round(val,1)}%" for val in df_filtered_2[F_bar_cols].values[0]], 
                        textposition='auto', name = "Barres (F)", hoverinfo="x+text"), row=2, col=2)
    
    fig.add_trace(go.Bar(x=['Plus '+ a.split()[0] for a in F_moy_max_min], y=df_filtered_1[F_moy_max_min].values[0],
                         text= [val for val in df_filtered_1[F_moy_max_min].values[0]], 
                         textposition='auto', name = "Forte&Faible Moy (F)" , hoverinfo="x+text"), row=2, col=3)


    # Troisième ligne : Garçons (M) - Élèves garçons uniquement
    fig.add_trace(go.Scatterpolar(r=df_filtered_2[M_cols].values[0], theta=[x[0:-2] for x in M_cols], fill='toself',
                                  text=[f"{np.round(val,1)}%" for val in df_filtered_2[M_cols].values[0]],
                                  marker=dict(size=10), name = "Radar (G)", hoverinfo="theta+text"), 
                                  row=3, col=1)


    fig.add_trace(go.Bar(x=M_bar_cols, y=df_filtered_2[M_bar_cols].values[0],
                         text=[f"{np.round(val,1)}%" for val in df_filtered_2[M_bar_cols].values[0]], 
                         textposition='auto', name = "Barres (G)", hoverinfo="x+text"), row=3, col=2)
    

    fig.add_trace(go.Bar(x=["Plus " + b.split()[0] for b in M_moy_max_min], y=df_filtered_1[M_moy_max_min].values[0],
                            text= [val for val in df_filtered_1[M_moy_max_min].values[0]], 
                            textposition='auto', name = "Forte&Faible Moy (G)", hoverinfo="x+text"), row=3, col=3)   
    
    # Mise à jour de la mise en page pour ajuster la taille
    fig.update_layout(
        title_text=f"Tableau de bord des résultats scolaires : {college} - Promotion {promotion}",
        height=1100,
        margin=dict(l=20, r=20, t=200, b=10),
        xaxis2=dict(domain=[0.38, 0.8]),
        xaxis3=dict(domain=[0.85, 1]),
        xaxis4=dict(domain=[0.38, 0.8]),
        xaxis5=dict(domain=[0.85, 1]),
        showlegend=True,
        #polar=dict( radialaxis=dict(visible=True,range=[0,100], angle=45, tickvals=[0, 25, 50, 75, 100]))
        )
    
    # Ajuster les marges internes des sous-graphiques pour ajouter de l'espace entre le titre et le graphique
    fig.update_annotations(font=dict(size=13, color = "blue"), 
                            showarrow=True, arrowhead=2, arrowcolor = "blue", yshift=15)  # Yshift ajoute de l'espace sous le titre

    # Afficher le graphique
    return fig
    
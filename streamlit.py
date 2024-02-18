import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Carregando os dados
df = pd.read_csv('Tour_Winners_data_1.csv')

# Configurando a página
st.title('Tour de France: Análise de Vencedores')
st.write('Fonte: https://www.kaggle.com/datasets/gulliverwoods/tour-de-france-winner-data')

st.write(df)

col1, col2, col3 = st.columns(3)
col4 = st.columns(1)

with col1:
    age_counts = df['age'].value_counts().sort_index().reset_index()
    age_counts.columns = ['Idade', 'Número de Vitórias']
    fig1 = px.bar(age_counts, x='Idade', y='Número de Vitórias',
                  title="Vitórias por Idade do Vencedor",
                  labels={'Número de Vitórias': 'Número de Vitórias'})
    fig1.update_traces(marker_color='#3498db', marker_line_color='#2980b9',
                       marker_line_width=1.5)
    st.plotly_chart(fig1, use_container_width=True)

    winner_counts = df['Winner'].value_counts().head(5).reset_index()
    winner_counts.columns = ['Vencedor', 'Número de Vitórias']
    fig4 = px.bar(winner_counts, x='Vencedor', y='Número de Vitórias',
                  title="Top 5 Maiores Vencedores",
                  labels={'Número de Vitórias': 'Número de Vitórias'})
    fig4.update_traces(marker_color='#e74c3c', marker_line_color='#c0392b',
                       marker_line_width=1.5)
    st.plotly_chart(fig4, use_container_width=True)

with col2:
    country_counts = df['Country'].value_counts().reset_index()
    country_counts.columns = ['País', 'Número de Vitórias']
    fig5 = px.pie(country_counts.head(5), values='Número de Vitórias', names='País',
                  title="Top 5 Países com Mais Vencedores")
    fig5.update_traces(textposition='inside', textinfo='percent+label',
                       marker=dict(colors=['#f39c12', '#e67e22', '#d35400', '#16a085', '#27ae60']))
    st.plotly_chart(fig5, use_container_width=True)

    df_filtered = df[df['Year'].between(2010, 2023)]
    winner_counts = df_filtered['Winner'].value_counts().head(5).reset_index()
    winner_counts.columns = ['Vencedor', 'Número de Vitórias']
    fig6 = px.bar(winner_counts, x='Vencedor', y='Número de Vitórias',
                  title="Top 5 Maiores Vencedores (2010-2023)",
                  labels={'Número de Vitórias': 'Número de Vitórias'})
    fig6.update_traces(marker_color='#2ecc71', marker_line_color='#27ae60',
                       marker_line_width=1.5)
    st.plotly_chart(fig6, use_container_width=True)

with col3:
    team_counts = df['Team'].value_counts().head(5).reset_index()
    team_counts.columns = ['Time', 'Número de Vitórias']
    fig7 = px.bar(team_counts, x='Time', y='Número de Vitórias',
                  title="Top 5 Times com Mais Vitórias",
                  labels={'Número de Vitórias': 'Número de Vitórias'})
    fig7.update_traces(marker_color='#9b59b6', marker_line_color='#8e44ad',
                       marker_line_width=1.5)
    st.plotly_chart(fig7, use_container_width=True)

    df_filtered = df[df['Year'].between(2010, 2023)]
    team_counts = df_filtered['Team'].value_counts().head(5).reset_index()
    team_counts.columns = ['Time', 'Número de Vitórias']
    fig8 = px.bar(team_counts, x='Time', y='Número de Vitórias',
                  title="Top 5 Times com Mais Vitórias (2010-2023)",
                  labels={'Número de Vitórias': 'Número de Vitórias'})
    fig8.update_traces(marker_color='#f1c40f', marker_line_color='#f39c12',
                       marker_line_width=1.5)
    st.plotly_chart(fig8, use_container_width=True)

with col4[0]:
    df_filtered = df[df['Year'].between(2000, 2023)]
    df_filtered['Tour_overall_length_(km)'] = pd.to_numeric(
        df_filtered['Tour_overall_length_(km)'], errors='coerce')
    df_filtered.dropna(subset=['Tour_overall_length_(km)'], inplace=True)
    tour_length = df_filtered.groupby(
        'Year')['Tour_overall_length_(km)'].mean().reset_index()
    fig10 = px.line(tour_length, x='Year', y='Tour_overall_length_(km)',
                    title="Média do Comprimento do Tour de France (2000-2023)",
                    labels={
                        'Tour_overall_length_(km)': 'Comprimento Médio (km)', 'Year': 'Ano'},
                    line_shape='spline')
    fig10.update_traces(line_color='#2ecc71', line_width=3)
    st.plotly_chart(fig10, use_container_width=True)
    st.write('Média do Comprimento do Tour de France (2000-2023):',
             round(tour_length['Tour_overall_length_(km)'].mean(), 2), 'km')

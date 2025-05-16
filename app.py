"""
Aplicação principal do Dashboard de Criptomoedas.
Este módulo contém a interface Streamlit para exibição dos dados das criptomoedas.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time

# Importando módulos locais
from api import get_top_cryptocurrencies
from utils import format_currency, format_percentage, create_dataframe, export_to_csv

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Criptomoedas",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Função para aplicar estilo personalizado
def local_css():
    st.markdown("""
    <style>
    .main {
        background-color: #FFFFFF;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    h1, h2, h3 {
        color: #6200EE;
    }
    .stButton>button {
        background-color: #6200EE;
        color: white;
    }
    .stDataFrame {
        border-radius: 5px;
    }
    .positive {
        color: green;
    }
    .negative {
        color: red;
    }
    </style>
    """, unsafe_allow_html=True)

# Aplicar estilo personalizado
local_css()

# Título e descrição
st.title("📊 Dashboard de Criptomoedas")
st.markdown("""
Este dashboard exibe informações atualizadas sobre as principais criptomoedas do mercado.
Os dados são obtidos em tempo real através da API da CoinMarketCap.
""")

# Sidebar
st.sidebar.header("Configurações")

# Número de criptomoedas a serem exibidas
num_cryptos = st.sidebar.slider("Número de criptomoedas", min_value=5, max_value=20, value=10, step=1)

# Botão para atualizar dados
if st.sidebar.button("🔄 Atualizar Dados"):
    st.experimental_rerun()

# Exibir hora da última atualização
st.sidebar.markdown(f"**Última atualização:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

# Função principal para carregar e exibir dados
def load_data():
    with st.spinner("Carregando dados das criptomoedas..."):
        try:
            # Obter dados da API
            crypto_data = get_top_cryptocurrencies(limit=num_cryptos)
            
            # Criar DataFrame
            df = create_dataframe(crypto_data)
            
            return df
        except Exception as e:
            st.error(f"Erro ao carregar dados: {e}")
            return None

# Carregar dados
df = load_data()

if df is not None:
    # Exibir visão geral do mercado
    st.header("Visão Geral do Mercado")
    
    # Criar colunas para métricas
    col1, col2, col3 = st.columns(3)
    
    # Calcular métricas
    total_market_cap = df['market_cap'].sum()
    avg_change_24h = df['variação_24h'].mean()
    total_volume_24h = df['volume_24h'].sum()
    
    # Exibir métricas
    col1.metric("Capitalização Total", format_currency(total_market_cap))
    col2.metric("Variação Média 24h", format_percentage(avg_change_24h))
    col3.metric("Volume Total 24h", format_currency(total_volume_24h))
    
    # Exibir tabela de criptomoedas
    st.header("Top Criptomoedas")
    
    # Formatar dados para exibição
    display_df = df.copy()
    display_df['preço'] = display_df['preço'].apply(lambda x: format_currency(x))
    display_df['variação_24h'] = display_df['variação_24h'].apply(lambda x: format_percentage(x))
    display_df['volume_24h'] = display_df['volume_24h'].apply(lambda x: format_currency(x))
    display_df['market_cap'] = display_df['market_cap'].apply(lambda x: format_currency(x))
    
    # Reordenar e renomear colunas para exibição
    display_df = display_df[['rank', 'nome', 'símbolo', 'preço', 'variação_24h', 'volume_24h', 'market_cap']]
    display_df.columns = ['Rank', 'Nome', 'Símbolo', 'Preço', 'Variação 24h', 'Volume 24h', 'Capitalização']
    
    # Exibir tabela
    st.dataframe(display_df, use_container_width=True)
    
    # Gráfico de barras para capitalização de mercado
    st.header("Capitalização de Mercado")
    fig_market_cap = px.bar(
        df.sort_values('market_cap', ascending=False).head(10),
        x='nome',
        y='market_cap',
        color='market_cap',
        color_continuous_scale='Purples',
        labels={'nome': 'Criptomoeda', 'market_cap': 'Capitalização de Mercado (USD)'}
    )
    fig_market_cap.update_layout(
        xaxis_title="Criptomoeda",
        yaxis_title="Capitalização de Mercado (USD)",
        height=500
    )
    st.plotly_chart(fig_market_cap, use_container_width=True)
    
    # Gráfico de variação percentual em 24h
    st.header("Variação em 24h")
    fig_change = px.bar(
        df.sort_values('variação_24h'),
        x='nome',
        y='variação_24h',
        color='variação_24h',
        color_continuous_scale='RdBu',
        labels={'nome': 'Criptomoeda', 'variação_24h': 'Variação em 24h (%)'}
    )
    fig_change.update_layout(
        xaxis_title="Criptomoeda",
        yaxis_title="Variação em 24h (%)",
        height=500
    )
    st.plotly_chart(fig_change, use_container_width=True)
    
    # Exportar para CSV
    st.header("Exportar Dados")
    if st.button("📥 Exportar para CSV"):
        csv_file = export_to_csv(df)
        with open(csv_file, "rb") as file:
            st.download_button(
                label="📄 Baixar CSV",
                data=file,
                file_name="crypto_data.csv",
                mime="text/csv"
            )

# Rodapé
st.markdown("---")
st.markdown("""
<div style="text-align: center">
    <p>Dashboard desenvolvido para fins educacionais | Dados fornecidos pela API da CoinMarketCap</p>
</div>
""", unsafe_allow_html=True)

"""
Módulo de utilidades para o dashboard de criptomoedas.
Este módulo contém funções auxiliares para processamento e formatação de dados.
"""
import pandas as pd
from typing import Dict, List, Any

def format_currency(value: float) -> str:
    """
    Formata um valor para exibição como moeda.
    
    Args:
        value (float): Valor a ser formatado.
        
    Returns:
        str: Valor formatado como moeda.
    """
    if value >= 1_000_000_000:
        return f"US$ {value / 1_000_000_000:.2f} bi"
    elif value >= 1_000_000:
        return f"US$ {value / 1_000_000:.2f} mi"
    elif value >= 1_000:
        return f"US$ {value / 1_000:.2f} mil"
    else:
        return f"US$ {value:.2f}"

def format_percentage(value: float) -> str:
    """
    Formata um valor para exibição como porcentagem.
    
    Args:
        value (float): Valor a ser formatado.
        
    Returns:
        str: Valor formatado como porcentagem.
    """
    return f"{value:.2f}%"

def create_dataframe(crypto_data: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Cria um DataFrame pandas a partir dos dados de criptomoedas.
    
    Args:
        crypto_data (List[Dict[str, Any]]): Lista de dados de criptomoedas.
        
    Returns:
        pd.DataFrame: DataFrame com os dados formatados.
    """
    data = []
    
    for crypto in crypto_data:
        data.append({
            'id': str(crypto['id']),
            'rank': crypto['cmc_rank'],
            'nome': crypto['name'],
            'símbolo': crypto['symbol'],
            'preço': crypto['quote']['USD']['price'],
            'variação_24h': crypto['quote']['USD']['percent_change_24h'],
            'volume_24h': crypto['quote']['USD']['volume_24h'],
            'market_cap': crypto['quote']['USD']['market_cap'],
        })
    
    return pd.DataFrame(data)

def export_to_csv(df: pd.DataFrame, filename: str = "crypto_data.csv") -> str:
    """
    Exporta o DataFrame para um arquivo CSV.
    
    Args:
        df (pd.DataFrame): DataFrame a ser exportado.
        filename (str, optional): Nome do arquivo. Padrão é "crypto_data.csv".
        
    Returns:
        str: Caminho do arquivo salvo.
    """
    df.to_csv(filename, index=False)
    return filename

"""
Módulo para interação com a API da CoinMarketCap.
Este módulo contém funções para obter dados das principais criptomoedas.
"""
import requests
import json
from typing import Dict, List, Any

# Chave da API fornecida (apenas para uso educacional)
API_KEY = "a544d070-5230-4ac6-8872-eb6bc62177a4"

# URLs base da API
BASE_URL = "https://pro-api.coinmarketcap.com/v1"
LATEST_URL = f"{BASE_URL}/cryptocurrency/listings/latest"
METADATA_URL = f"{BASE_URL}/cryptocurrency/info"

def get_headers() -> Dict[str, str]:
    """
    Retorna os cabeçalhos necessários para as requisições à API.
    
    Returns:
        Dict[str, str]: Dicionário com os cabeçalhos da requisição.
    """
    return {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY,
    }

def get_top_cryptocurrencies(limit: int = 10) -> List[Dict[str, Any]]:
    """
    Obtém dados das principais criptomoedas da CoinMarketCap.
    
    Args:
        limit (int, optional): Número de criptomoedas a serem retornadas. Padrão é 10.
        
    Returns:
        List[Dict[str, Any]]: Lista de dicionários com dados das criptomoedas.
        
    Raises:
        Exception: Se ocorrer um erro na requisição à API.
    """
    parameters = {
        'start': '1',
        'limit': str(limit),
        'convert': 'USD'
    }
    
    try:
        response = requests.get(LATEST_URL, headers=get_headers(), params=parameters)
        data = response.json()
        
        if response.status_code == 200:
            return data['data']
        else:
            raise Exception(f"Erro na API: {data.get('status', {}).get('error_message', 'Erro desconhecido')}")
            
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erro na requisição: {e}")
    except (KeyError, json.JSONDecodeError) as e:
        raise Exception(f"Erro ao processar dados: {e}")

def get_cryptocurrency_metadata(crypto_ids: List[str]) -> Dict[str, Any]:
    """
    Obtém metadados adicionais para as criptomoedas especificadas.
    
    Args:
        crypto_ids (List[str]): Lista de IDs das criptomoedas.
        
    Returns:
        Dict[str, Any]: Dicionário com metadados das criptomoedas.
        
    Raises:
        Exception: Se ocorrer um erro na requisição à API.
    """
    parameters = {
        'id': ','.join(crypto_ids)
    }
    
    try:
        response = requests.get(METADATA_URL, headers=get_headers(), params=parameters)
        data = response.json()
        
        if response.status_code == 200:
            return data['data']
        else:
            raise Exception(f"Erro na API: {data.get('status', {}).get('error_message', 'Erro desconhecido')}")
            
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erro na requisição: {e}")
    except (KeyError, json.JSONDecodeError) as e:
        raise Exception(f"Erro ao processar dados: {e}")

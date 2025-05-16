# 🚀 CryptoVision Dashboard


<div align="center">
 <img src="https://github.com/user-attachments/assets/412db07c-e956-40ce-a97e-030fe6049488" alt="CryptoVision Dashboard" width="800">

</div>

## 💡 Sobre o Projeto

O **CryptoVision Dashboard** é uma aplicação web interativa desenvolvida em Python que permite visualizar dados em tempo real das principais criptomoedas do mercado. Este projeto demonstra a implementação de um dashboard completo utilizando a API da CoinMarketCap, com visualizações dinâmicas e análises de dados financeiros.

### 🔍 Principais Recursos

- **Monitoramento em Tempo Real**: Acompanhe os preços e variações das top criptomoedas
- **Visualização de Dados Avançada**: Gráficos interativos para análise de capitalização e tendências
- **Interface Responsiva**: Design moderno e adaptável a diferentes dispositivos
- **Exportação de Dados**: Funcionalidade para exportar dados em formato CSV
- **Atualizações Instantâneas**: Botão para atualizar dados sob demanda

## 🛠️ Tecnologias Utilizadas

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/API-REST-009688?style=for-the-badge&logo=api&logoColor=white" alt="REST API">
</div>

- **Backend**: Python 3.11 para processamento de dados e lógica de negócios
- **Frontend**: Streamlit para interface web interativa e responsiva
- **Visualização**: Plotly para gráficos dinâmicos e interativos
- **Dados**: Pandas para manipulação e análise de dados
- **API**: Integração com a API da CoinMarketCap via Requests
- **Estilização**: CSS personalizado para tema profissional

## ⚙️ Arquitetura do Projeto

O projeto segue uma arquitetura modular e bem organizada:

```
crypto_dashboard/
│
├── app.py                # Aplicação principal e interface Streamlit
├── api.py                # Módulo de integração com a API da CoinMarketCap
├── utils.py              # Funções utilitárias para processamento de dados
├── requirements.txt      # Dependências do projeto
└── screenshots/          # Capturas de tela do dashboard
```

## 📊 Funcionalidades Implementadas

- **Dashboard Principal**: Visão geral do mercado de criptomoedas
- **Tabela Interativa**: Listagem das top criptomoedas com dados detalhados
- **Métricas em Tempo Real**: Capitalização total, variação média e volume
- **Gráficos de Capitalização**: Visualização comparativa entre as principais moedas
- **Gráficos de Variação**: Análise de performance em períodos de 24h
- **Exportação de Dados**: Funcionalidade para salvar dados em CSV
- **Personalização**: Interface com tema profissional em branco e roxo

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.6 ou superior
- Pip (gerenciador de pacotes do Python)

### Instalação

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/cryptovision-dashboard.git
cd cryptovision-dashboard
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv

# No Windows
venv\Scripts\activate

# No Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute a aplicação:
```bash
streamlit run app.py
```

5. Acesse o dashboard no navegador (geralmente em http://localhost:8501)

## 🧠 Aprendizados e Desafios

Durante o desenvolvimento deste projeto, pude aprimorar diversas habilidades técnicas:

- **Consumo de APIs REST**: Implementação de requisições autenticadas e tratamento de respostas
- **Manipulação de Dados Financeiros**: Processamento e formatação de dados de mercado
- **Visualização Interativa**: Criação de gráficos dinâmicos para análise de dados
- **Design de Interface**: Desenvolvimento de UI/UX intuitiva e responsiva
- **Modularização de Código**: Estruturação do projeto em componentes reutilizáveis

## 🔮 Melhorias Futuras

- Implementação de autenticação de usuários
- Adição de histórico de preços com séries temporais
- Criação de alertas personalizados de preço
- Integração com múltiplas fontes de dados
- Implementação de análises preditivas com machine learning

## 📜 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.

## 📬 Contato

- LinkedIn: [Caio Venancio](https://www.linkedin.com/in/caio-venancio/)
- GitHub: [@CaioVenxncio](https://github.com/CaioVenxncio)
- Email: caiovenanciocommercial@gmail.com

---

<div align="center">
  <p>Desenvolvido com ❤️ e ☕</p>
</div>


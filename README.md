# Projeto de Análise de Expiração de Contratos Futuros da B3

Este projeto consiste em um sistema desenvolvido em Python capaz de analisar as regras de expiração de contratos futuros da B3, a bolsa de valores brasileira. O sistema lê os códigos dos ativos de um arquivo Excel e armazena as datas de expiração correspondentes em uma coluna do mesmo arquivo.

## Instalação e Configuração
Para utilizar o projeto, é necessário instalar as seguintes bibliotecas:

pandas
pandas_market_calendars

Essas bibliotecas podem ser instaladas através do gerenciador de pacotes pip:
```pip install pandas numpy pandas_market_calendars```
## Exemplo de Uso
Suponha que você tenha um arquivo Excel chamado symbols.xlsx com os códigos dos ativos na coluna A e outras informações na coluna B. Para executar o projeto, basta executar o seguinte comando no terminal:
python main.py symbols.xlsx

O script lerá o arquivo symbols.xlsx, analisará as regras de expiração dos contratos futuros correspondentes aos códigos de ativo presentes na coluna A e armazenará as datas de expiração correspondentes na coluna E do mesmo arquivo.



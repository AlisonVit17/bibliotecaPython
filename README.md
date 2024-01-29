# bibliotecaPython

Estes scripts Python bibliotecaMagalu e bibliotecaMercadeLivre permitem realizar buscas por produtos na Magazine Luiza e no Mercado Livre, filtrando por nome e preço máximo desejado. Utiliza a biblioteca BeautifulSoup para fazer o parsing das respectivas páginas HTML dos sites.

Como Usar:

1 - Clone o repositório para o seu ambiente local:
        -> git clone https://github.com/seu-usuario/bibliotecaPython.git
        -> cd bibliotecaPython
        
2 - Instale as dependências necessárias:
        -> pip install BeautifulSoap
        -> pip install Requests

3 - Execute o script:
        -> python3 bibliotecaMercadoLivre.py

4. Siga as instruções fornecidas para inserir o título da busca e o preço máximo.

5. Os resultados da busca serão exibidos, mostrando links e preços dos produtos que atendem aos critérios especificados.


Exemplo de Uso:

from bs4 import BeautifulSoup
import requests
from bibliotecaMercadoLivre import buscarNoMercadoLivre

# Realiza uma busca por smartphones com preço máximo de R$ 1500.00
nomeBusca = "smartphone"
valorBusca = 1500.00
lista_resultados = buscarNoMercadoLivre(nomeBusca, valorBusca)

# Imprime os resultados
for i, produto in enumerate(lista_resultados, start=1):
    print(f"{i}. Link: {produto[0]}, Preço: R${produto[1]:.2f}")

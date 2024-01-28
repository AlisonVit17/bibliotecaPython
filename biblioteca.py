import requests
from bs4 import BeautifulSoup

def buscarNaMagalu(nomeDaBusca, precoBusca):

    #Importando o link:
    link = 'https://www.magazineluiza.com.br/busca/' + nomeDaBusca + '/' #Link para a busca simples na magalu
    requisicao = requests.get(link) #Importação do link
    print(requisicao)
    print(link)

    site = BeautifulSoup(requisicao.text, "html.parser") #Pra ficar na estrutura normal do html

    pesquisa = site.find_all("li", "sc-kTbCBX ciMFyT")
    precos = site.find_all("div", "sc-dhKdcB ryZxx")
    #print(requisicao.text)
    #print(site)
    listaDeValores = []
    listaRetorno = []
    for preco in precos:
        
        valor = str(preco).split("<")
        valor = valor[2].split(">")
        valor = valor[1].split()
        listaAuxiliar = ''
        for a in valor:
            listaAuxiliar = a

        print(listaAuxiliar)
        
        listaAuxiliar = listaAuxiliar.replace(',', '.') #Troca as ',' pelos '.'
        listaAuxiliar = listaAuxiliar.split('.') # Tira os pontos do valor, separando os números em índices da lista
        valorFinal = '' #Responsável por pegar o número
        for i in listaAuxiliar:
                
            valorFinal += i
        listaDeValores.append(float(valorFinal) / 100.0)
        print(float(valorFinal) / 100.0)
        print(a.split())        
        
    for i, pesq in enumerate(pesquisa):

        if len(listaDeValores) < i:
            break
        linkBusca = 'https://www.magazineluiza.com.br/'
        linkBusca += pesq.a['href']
        if listaDeValores[i] < precoBusca:
            
            listaRetorno.append((linkBusca, listaDeValores[i])) 
        


    for i in listaRetorno:
        print(i[0],'  ', i[1])

    return listaRetorno


#Início, só para pegar os valores:
nomeDaBusca = input('Insira o que você busca: ')
precoBusca = float(input('Insira o preço que não pode ser ultrapassado: '))
retorno = buscarNaMagalu(nomeDaBusca, precoBusca)

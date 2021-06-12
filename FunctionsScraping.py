from bs4 import BeautifulSoup
from shutil import copyfileobj

import requests

def get_content(url):
    #Função que faz a requisição e retorna o conteudo da pagina
    html = requests.get(url)
    if html.status_code != 200:
        print("Falha na requisição!")
    else:
        content_html = BeautifulSoup(html.content, 'html.parser')
        return content_html


def download_file(url):
    #Função que faz a requisição e o download do arquivo
    name=url.split('/')
    file_="./"+name[-1]+".pdf"
    xpto=requests.get(url, stream=True)
    with open(file_,'wb') as save:
          copyfileobj(xpto.raw,save)
    print("Arquivo baixado com sucesso!")
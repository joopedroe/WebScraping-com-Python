from FunctionsScraping import *

base_url="http://www.ans.gov.br"

#Encontra o link para proxima pagina
content_page1 = get_content("http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar/")
div_ = content_page1.find("div", attrs={'class':'alert alert-icolink'})
link_page2=div_.find("a").get('href')

#Na segunda pagina, encontra o link para o download do arquivo
content_page2 = get_content(base_url+link_page2)
link = content_page2.find("a", attrs={'class':'btn btn-primary btn-sm center-block'})
link_PDF=link.get('href')

#Faz o download do aquivo a partir do link
download_file(base_url+link_PDF)





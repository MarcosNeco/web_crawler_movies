<h1>Tecnologias e Bibliotecas</h1>
<ul>
 <li>Python 3.7.2</li>
 <li>MongoDB</li>
 <li>BeautifulSoup</li>
 <li>Requests</li>
 <li>Pymongo</li>
 <li>flask</li>
</ul>

<h1>Introdução</h1>

 Esse projeto tem como objetivo indexar uma quantidade x de páginas de filmes, do site www.imdb.com. Após indexa-las
 é feito uma extração de suas propriedades para tirar informações como nome do filme, diretor, nota dada ao filme de
 acordo com informações dos usuários.
 
 <h1>Fluxo Sistema</h1>
 O sistema funciona executando de tempo em tempo uma busca no site de filmes, após fazer essa busca e indexar algumas páginas,
 são extraídos informações das páginas através do parseamento do html. Para requisição das páginas é utilizado a api requests e 
 para parseamento do html é utilizado a api <strong>BeautifulSoup</strong>. Após isso, essas propriedades são convertidas em objetos 
 python para que haja a atualização ou insersação dos dados no banco mongoDB. Só são indexadas 10000 páginas, após a insersação dessa
 quantidade de documentos no mongo, o processo para de indexar.
 Além disso, existe um WS que pode ser acessado localmente no endereço http:localhost:8080/, que são exibidas respondidas algumas perguntas referentes aos documentos armezanados no mongo, como por exemplo a média de duração dos filmes.
 
 
 <h1>MongoDB</h1>
 Para o banco mongo foi utilizado sua versão na nuvem, que fica hospedado na url https://mlab.com/, para esse projeto foi criado um database especefício e uma collection especifíca.

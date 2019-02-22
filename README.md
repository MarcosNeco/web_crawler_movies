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
 Além disso, existe um WS que pode ser acessado localmente no endereço http:localhost:8080/, que são exibidas respondidas algumas perguntas referentes aos filmes armezanados no mongo, como por exemplo a média de duração dos filmes.
 
 
<h1>MongoDB</h1>
 Para o banco mongo foi utilizado sua versão na nuvem, que fica hospedado na url https://mlab.com/, para esse projeto foi criado um database especefício e uma collection especifíca. É possível passar a url de conexão com o mongo na inicialização do script python, caso contrário ele ira assumir o defaul hospedado na nuvem.
 
<h1>Testes Unitários</h1>
Foram criados testes unitários para duas classes em especifíco, a classe principal que contém o código de indexação:

```WebCrawlerTest.py```

E para o teste de extração de propriedades das páginas de filme foi criado o teste:

```ExtractorAttributesPageTest.py```

<h1>Execução scripts</h1>
Existem dois scripts que podem iniciados individualmente, um deles é:

```IndexerStart.py```

Através desse script é iniciado processo de navegar entre as páginas e encontrar urls que pertencem aos filmes, para só então converter para um objeto válido e persistir no mongo.
O segundo script é:

```WSStart.py```

Esse script pode ser executado em paralelo a execução do anterior, já que ele executa consultas no banco mongo e faz consultas neles para extraír algumas informações interessantes, ou seja, o processo de indexar e apresentar as informações não são acoplados. Após rodar o script, as informações extraídas podem ser acessadas na url: http://localhost:8080/.

<h1>Evoluções</h1>
<ul>
 <li>Implementar um controle de quais as urls já foram salvas no banco, para que não seja necessário indexá-las novamente.
 <li>Encontrar em alguma outra fonte a propriedade de gênero dos diretores dos filmes, já que no site imdb não possui essa informação.
 <li>Otimizar as consultas para que a página inicial não leve tanto tempo para carregar, já que as consultas são realizadas no banco a cada refresh executado na página</li>
</ul>


Cadastrar uma pessoa

POST /catalogo/pessoas
{
    "nome": "João Silva",
    "interesses": ["futebol", "música", "literatura"],
    "cidade": "São Paulo",
    "formacao": "Letras",
    "estado": "SP",
    "pais": "Brasil"
}

Informar ao elasticsearch de que não desejamos replicas os dados desse índice (/catalogo) em outras máquinas.

Isso já que estamos rodando o elasticsearch local.

PUT /catalogo/_settings
{
    "index": {
        "number_of_replicas": 0
    }
}

Acessar a quantidade de registros em um índice

GET /catalogo/pessoas/_count
{}

Cadastrar uma pessoa informado o ID

POST /catalogo/pessoas/1
{
    "nome": "João Silva",
    "interesses": ["futebol", "música", "literatura"],
    "cidade": "São Paulo",
    "formacao": "Letras",
    "estado": "SP",
    "pais": "Brasil"
}

Buscar uma pessoa informado o ID

GET /catalogo/pessoas/1
{}

Buscar todos os documentos de um índice

GET /catalogo/pessoas/_search
{}

Buscar todos os documentos com filtro por campo

GET /catalogo/pessoas/_search?q=futebol
{}

Informar se o documento existe ou não.
Observação.
Se retornar 200 o registro existe
Se retornar 404 o registro não existe

curl -X HEAD -v http://localhost:9200/catalogo/pessoas/1

Insert ou update total

PUT /catalogo/pessoas/100
{
    "nome": "Thadeu",
    "interesses": ["futebol", "música", "programação"],
    "cidade": "São Paulo",
    "formacao": "Ciência da Computação",
    "estado": "ON",
    "pais": "Canadá"
}


Excluir um registro

DELETE /catalogo/pessoas/100
{}


Update parcial

POST /catalogo/pessoas/100/_update
{
    "doc": {
        "nome": "Thadeu"
    }
}




Analise o seguinte comando:

curl -XHEAD -v http://localhost:9200/catalogo/pessoas/1COPIAR CÓDIGO
O que exatamente ele faz?

RESPONDA
Opinião do instrutor

O comando HEAD não retorna conteúdo, ele verifica se o documento, cujo identificador é ID (no exemplo do exercício, o ID é 1), existe para o tipo TYPE (no exemplo do exercício, o TYPE é pessoas) no índice INDEX (no exemplo do exercício, o INDEX é catalogo). Caso o documento exista, é retornado o código HTTP 200 , caso contrário, é retornado o código HTTP 404.








Rode um comando PUT para uma URI sem id, por exemplo:

PUT /catalogo/pessoas/

{
    "nome": "João Silva",
    "interesses": [
        "futebol",
        "música",
        "literatura"
    ],
    "cidade": "São Paulo",
    "formação": "Letras",
    "estado": "SP",
    "país": "Brasil"
}COPIAR CÓDIGO
O que acontece?

RESPONDA
Opinião do instrutor

Um erro acontece, com a seguinte mensagem: "No handler found for uri [//catalogo/pessoas/] and method [PUT]"

Isso ocorre pois o id no comando PUT é obrigatório. Caso já exista um documento com esse id, o documento será substituído. Caso não exista um documento com esse id, ele será criado.


---



Busca com filtro (where)

GET /catalogo/pessoas/_search?q=futebol
{}




---



























Para atualizar, modificar o atributo nome do documento de id 1 para Douglas Quintanilha, que comando e URI devemos utilizar?

Alternativa correta
GET /catalogo/pessoas/1/_update
{
    "doc": {
        "nome": "Douglas Quintanilha"
    }
}
Alternativa correta
POST /catalogo/pessoas/1
{
    "nome": "Douglas Quintanilha"
}
Alternativa correta
PUT /catalogo/pessoas/1/_update
{
    "doc": {
        "nome": "Douglas Quintanilha"
    }
}
Alternativa correta
PUT /catalogo/pessoas/1
{
    "nome": "Douglas Quintanilha"
}
Alternativa correta
POST /catalogo/pessoas/1/_update
{
    "doc": {
        "nome": "Douglas Quintanilha"
    }
}
O comando e URI que devemos utilizar é:

POST /catalogo/pessoas/1/_update
{
    "doc": {
        "nome": "Douglas Quintanilha"
    }
}COPIAR CÓDIGO
Para atualizar somente um ou mais atributos, devemos utilizar a sintaxe acima, passar os atributos, juntamente com os seus novos valores, dentro de um "doc". Além disso, como queremos somente atualizar o documento, temos que adicionar o \_update na URI e utilizar o comando POST.

Como dito anteriormente, o PUT substitui o documento, ou seja, se fizermos:

PUT /catalogo/pessoas/1
{
    "nome": "Douglas Quintanilha"
}COPIAR CÓDIGO
Substituiremos o documento de id, logo ele só conterá o atributo nome.

Vale lembrar que uma vez que um documento é criado em uma instância do ElasticSearch, este documento torna-se imutável. No caso de uma atualização a um documento existente, por exemplo como fizemos com o método POST, uma nova versão do documento é criada. Se repararmos bem nas respostas recebidas, notaremos os atributos _created e _version. A resposta para a criação de um novo documento possui _created = true e _version = 1. A resposta para atualizações possui _created = false e _version será a versão anterior do documento acrescida de 1.









Visitando a página Cluster do Kopf, é possível ter uma visão de como é o nosso cluster. Ela mostra todas as máquinas, assim como os seus índices, e as shards de cada índice. Uma pergunta que podemos nos fazer é, qual seria a quantidade de shards necessária para o nosso índice?

RESPONDA
Opinião do instrutor

O número de shards de um índice é definido no momento da criação do mesmo, e não pode ser alterado. Por isso é muito importante escolher bem o número de shards durante a criação do índice. Mas este número depende do volume de informações que serão armazenadas nas shards, logo esse volume é dividido pela quantidade de shards desejada, vendo assim o quão grande cada shard será.

Na prática, isso significa que muitas shards auxiliam na hora da escrita, mas o desempenho pode ser afetado na hora da leitura, pois uma busca terá que ler muitas shards para confirmar se as informações foram encontradas ou não, por exemplo. Por isso que depende da frequência em que se escreve e que se lê na shard, mas um shard não deve exceder o volume de 50 gb.

No nosso treinamento, vamos utilizar o número padrão de shards, que é cinco shards.









Nós sabemos que quando criamos um documento no ElasticSearch, sua versão inicial possui o valor 1. Após uma atualização qualquer, a versão é automaticamente incrementada para 2. Agora imagine duas pessoas diferentes querendo atualizar este documento de formas diferentes. Como prevenir a perda acidental de informação?

RESPONDA
Opinião do instrutor

ElasticSearch possui um controle de versionamento baseado em lock otimista. Basicamente funciona assim. Quando utilizado este mecanismo, uma atualização só ocorre com sucesso quando a versão do documento no ElasticSearch é a mesma da versão do documento indicado na requisição. Por exemplo:

PUT /catalogo/pessoas/1?version=1
{
    … atributos a serem atualizados
}COPIAR CÓDIGO
Caso alguém já tenha atualizado o documento, a versão terá sido incrementada para 2 e nossa requisição falhará. O código HTTP de resposta será 409 Conflict e a mensagem de erro será algo como:

{
    "error" : "VersionConflictEngineException[[catalogo][2] [pessoas][1]: version conflict, current [2], provided [1]]",
    "status" : 409
}COPIAR CÓDIGO
ElasticSearch permite que um sistema de versionamento externo, como por exemplo o uso de timestamps seja utilizado. Para saber mais, visite este a página https://www.elastic.co/guide/en/elasticsearch/guide/current/optimistic-concurrency-control.html






Buscar todos os documentos com filtro por valor em todos os campos

_all implícito
GET /catalogo/pessoas/_search?q=futebol
{}

_all explícito
GET /catalogo/pessoas/_search?q=_all:futebol
{}

filtro por campo [explícito]
GET /catalogo/pessoas/_search?q=estado:SP
{}

filtro por mulitplos campos [explícito]

A sintaxe sempre é campo:termo , mas se queremos adicionar mais um campo para a busca, temos que utilizar o caractere & para unir as duas buscas, deste modo;

_search?q=interesses:futebol&cidade:rio

_search?q=interesses:futebol&cidade:rio

OBS: Todos os atributos do Elasticsearch são indexados por padrão! Isso significa que não precisamos criar índices para atributos em específico. E assim conseguimos realizar consultas mais rápidas.





Outro detalhe importante é em relação a quantidade de documentos retornados.
Por padrão, o ElasticSearch retorna até 10 documentos. Como temos menos documentos em nosso índice, temos a impressão que todos os resultados são sempre retornados.

SIZE (PAGINAÇÃO)
GET /catalogo/pessoas/_search?q=futebol&size=1
{}


Para limitarmos a quantidade de dados devemos utilizar o termo size, passando com o = a quantidade que queremos limitar.

Então, fazemos a buscar normal:

_search?q=interesses:futebol

mas vamos utilizar o operador & para adicionar um limite a busca com o size:

_search?q=interesses:futebol&size=50

Assim esta busca nos retornará apenas os primeiros 50 registros !



FROM (PAGINAÇÃO)  a partir de qual elemento o elasticsearch deve realizar a consulta?
GET /catalogo/pessoas/_search?q=futebol&size=1&from=0
{}

I M P O R T A N T E

Embora possamos ter paginação com elasticsearch, ao realizar uma consulta com x elementos.

O elasticsearch irá consultar e carregar todos os x documentos no index e retornar apenas o da página informada.

devolver 100 documentos a partir do primeiro



API Scroll
Quando utilizamos paginação simples, temos que tomar cuidado para não causarmos instabilidade no cluster. Caso solicitemos 10.000 registros, todas as shards participantes na consulta podem retornar esta quantidade. Por exemplo, caso tenhamos 3 shards com 100.000 documentos em cada e pedimos os primeiros 10.000 resultados, o nó coordenador terá de processar 30.000 documentos, executar a ordenação e pegar os primeiros 10.000.

Para detalhes, veja este link:

https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-scroll.html



---

COmo se fosse o desribe do SQL

_mapping

GET /catalogo/_mapping/pessoas
{}

En possível criar novos atributos em um tipo (tabela) já existente.

Porém não eh possívle alterar o tipo de dados de atributos já criados



PUT /catalogo/pessoas/1
{
    "nome": "João Silva",
    "interesses": ["futebol", "música", "literatura"],
    "cidade": "São Paulo",
    "formacao": "Letras",
    "estado": "SP",
    "pais": "Brasil",
    "nascimento": "2010-10-10"
}


---

Tipagem

core: strings, números, datas e etc

complexos: arrays, ipv4, ipv6, informação geo espacial, 



Repare o tipo strict_date_optional_time||epoch_millis que automaticamente foi interferido para o atributo nascimento.

Tipos suportados no ElasticSearch
ElasticSearch suporta diferentes tipos de atributos, inclusive alguns que vão te deixar meio surpresos. Já imaginou um tipo IPv4? Por hora, vamos focar apenas nos tipos que possuem valor direto para nosso projeto. Para mais informações, acesse o link https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-types.html.

Os tipos básico (também chamados de core) são:

Para texto: string
Para números: long, integer, short, byte, double e float.
Para datas: date. O formato padrão é strict_date_optional_time||epoch_millis, que signfica data com hora como opcional ou valor epoch em milisegundos.
Note que o formato da data pode ser customizado para garantir consistência no dado armazenado para buscas e outras operações.

Mais detalhes em https://www.elastic.co/guide/en/elasticsearch/reference/current/date.html.



PUT /catalogo/_mapping/pessoas
{
  "properties": {
    "pulo": {
      "type": "integer"
    }
  }
}

RESPONSE

{
  "acknowledged": true
}

---













GET /catalogo/pessoas/_search?q=musica
{}

---

quando trabalhamos com busca exata, o que interessa é saber "sim" ou "não".

Se os termos consultados casam com os dados dos indexes.


Já com full text search, o importante não é se o documento casa ou não casa perfeitamente com os termos da busca.

Mas sim o quanto que o documento casa com os termos da busca.

POr este motivo e leastic search possui o campo "max_score".

Quanto mais alto o valor do max_score, mais o documento está aderente a busca.

Sendo que o score vai de 0 a 1.



full text search => busca em texto cheio

Neste tipo de consulta, não estamos interessados apenas se o documento casa ou não com a consulta.

Estamos mais interessados em "quanto" o documento casa (correponde) a consulta (score).


---

Índice invertidos
Caso queira entender melhor como a busca de termos funciona quando utilizamos um índice invertido, veja o link: https://www.elastic.co/guide/en/elasticsearch/guide/current/inverted-index.html


---

Analyzer são algoritmos momificadores que são aplicados em todos os campos do documento (registros) persistidos no Elastic Search.

INdice invertido?

Analyzers Communs

- Espaço em branco: quebra string spor espaço em branco
O analyzer whitespace (ou analyzer de espaço em branco) quebra o texto por espaços em branco e não altera a caixa das letras
- Simples (simples): quebra o texto em palavras, descarta números, símbolos, (tudo que não for letra) e deixa o texto em caixa baixa (lower case).
- Padrão (standard): remove espaços, pontuações e deixa o texto em caixa baixa. Mas não remove números.
- Idioma (e.g.: portugês): 


---

heio. Quando fazemos buscas exatas o resultado é binário, ou seja, "sim" caso o termo procurado exista da maneira que foi informado ou "não", caso contrário. No caso de busca de texto cheio, a ideia é diferente. Ao invés de perguntarmos "Este documento possui exatamente os termos utilizados na busca", estamos interessados em "O quão bem este documento casa com os termos da busca".

Vamos ver alguns exemplos. No primeiro exemplo, queremos procurar pelo termo "EUA" mas estamos satisfeitos com documentos com os termos "Estados Unidos da América" ou "Estados Unidos". No segundo exemplo, queremos procurar pelo termo "musica", porém estamos satisfeitos se encontrarmos documentos com os termos "bossa nova", "rock", "pagode" e "samba", pois eles se relacionam com música.

Analyzers são utilizados para processar nossos documentos e construir uma estrutura comum no mundo de buscas chamada de índice invertido. De maneira simplista, podemos pensar nos analyzers como algoritmos que processam o texto e geram entradas relevantes com os termos do documento, possivelmente com sinônimos, no índice invertido. Estas entradas possuem ponteiros para o documento. Os termos consultados também passam pelos mesmos algoritmos e os termos processados são utilizados para fazer a busca contra o índice invertido. Este processo ficará bem claro em alguns instantes.

Analyzers existentes
ElasticSearch possui diversos analyzers pré-definidos que podem ser associados à atributos durante a criação do mapping para o tipo. Destacamos 4 analyzers que devemos conhecer.

Analyzer padrão: Este é o analyzer padrão usado pelo ElasticSearch e em geral funciona bem independente do idioma. Ele funciona quebrando o texto em palavras removendo pontuações e passando todo conteúdo para letras minúsculas. Números existentes no texto são mantidos. Por exemplo: "Eu nasci há 10 mil (sim, 10 mil) anos atrás" gera as seguintes entradas "eu", "nasci", "há", "10", "mil", "sim", "10", "mil", "anos", "atrás".

Analyzer simples: Quebra o texto em tudo o que não seja uma letra e passando todo o texto para letras minúsculas. Como números não são letras, eles não geram entradas. E.g.: "Eu nasci há 10 mil (sim, 10 mil) anos atrás" gera as seguintes entradas "eu", "nasci", "há", "mil", "sim", "mil", "anos", "atrás".

Analyzer de espaço em branco: Quebra o texto por espaços em branco. Não há alteração na caixa das letras. Por exemplo: "Eu nasci há 10 mil (sim, 10 mil) anos atrás" gera as seguintes entradas "Eu", "nasci", "há", "10", "mil", "(sim", "10", "mil)", "anos", "atrás".

Analyzers específicos para idiomas: São analyzers que quebram o texto assim como o analyzer padrão, porém são capazes de aplicar peculiaridades do idioma e melhorar a geração das entradas para um idioma em específico. Técnicas como singularização dos termos, remoção de palavras que não possuem relevância para o resultado, como palavras comuns do idioma e uso da palavra na sua forma mais raíz (conhecido como stemming), são aplicadas.

Como passo adicional, analyzers ainda podem ser customizados caso necessário. Para mais detalhes veja https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-analyzers.html

O mais legal é que existe uma API chamada _analyze que nos permite observar como um texto será analisado.


---

Eu nasci há 10 mil (sim, 10 mil) anos atrás

_analyze?analyzer=standard&text=Eu+nasci+há+10+mil+(sim,+10+mil)+anos+atrás

_analyze?analyzer=simple&text=Eu+nasci+há+10+mil+(sim,+10+mil)+anos+atrás

_analyze?analyzer=whitespace&text=Eu+nasci+há+10+mil+(sim,+10+mil)+anos+atrás

_analyze?analyzer=portuguese&text=Eu+nasci+há+10+mil+(sim,+10+mil)+anos+atrás




---

**CRIADNO ÍNDICE**

PUT /catalogo_v2

{
  "settings": {
    "index": {
      "number_of_shards": 3,
      "number_of_replicas": 0
    }
  },
  "mappings": {
    "pessoas_v2": {
      "_all": {
        "type": "string",
        "index": "analyzed",
        "analyzer": "portuguese"
      },
      "properties": {
        "cidade": {
          "type": "string",
          "index": "analyzed",
          "analyzer": "portuguese"
        },
        "estado": {
          "type": "string"
        },
        "formação": {
          "type": "string",
          "index": "analyzed",
          "analyzer": "portuguese"
        },
        "interesses": {
          "type": "string",
          "index": "analyzed",
          "analyzer": "portuguese"
        },
        "nome": {
          "type": "string",
          "index": "analyzed",
          "analyzer": "portuguese"
        },
        "país": {
          "type": "string",
          "index": "analyzed",
          "analyzer": "portuguese"
        }
      }
    }
  }
}

RESPONSE

{
  "acknowledged": true
}


---


GET /catalogo_v2/pessoas_v2/_search?q=música
{}

---

/catalogo_v2/pessoas_v2
{
    "nome": "João Silva",
    "interesses": ["futebol", "música", "literatura"],
    "cidade": "São Paulo",
    "formacao": "Letras",
    "estado": "SP",
    "pais": "Brasil"
}

---

/catalogo_v2/pessoas_v2/1
{
    "nome": "João Silva",
    "interesses": ["futebol", "música", "literatura"],
    "cidade": "São Paulo",
    "formação": "Letras",
    "estado": "SP",
    "país": "Brasil"
}

/catalogo_v2/pessoas_v2/2
{
    "nome": "Maria Silva",
    "interesses": ["pintura", "literatura", "teatro"],
    "cidade": "Diamantina",
    "formação": "Artes Plásticas",
    "estado": "MG",
    "país": "Brasil"
}

/catalogo_v2/pessoas_v2/3
{
    "nome": "Richard Edward",
    "interesses": ["matemática", "física", "música"],
    "cidade": "Boston",
    "formação": "Física",
    "estado": "MA",
    "país": "Estados Unidos"
}

/catalogo_v2/pessoas_v2/4
{
    "nome": "Patrick von Steppat",
    "interesses": ["computação", "culinária", "cinema"],
    "cidade": "Rio de Janeiro",
    "formação": "Gastronomia",
    "estado": "RJ",
    "país": "Brasil"
}

---

Como dito no enunciado, o padrão do ElasticSearch é buscar no documento um termo ou (OR, em inglês) outro. Para buscar documentos que contenham os dois termos (musica e brasil), nós precisamos utilizar o AND. Atenção para a caixa alta, se for em caixa baixa, o ElasticSearch interpretará como mais um termo a ser buscado.

GET
/catalogo_v2/pessoas_v2/_search?q=musica+AND+brasil



---

O campo _all pode ser totalmente customizado ou mesmo desabilitado. Neste capítulo nós trocamos o analyzer standard para o analyzer portuguese, porém podemos ir mais adiante e definir, por exemplo quais atributos devem ir para o campo _all e qual o peso (boost) de cada atributo em uma busca.

VER OPINIÃO DO INSTRUTOR
Opinião do instrutor

Para saber mais, acesse:

https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-all-field.html


---

Objetos aninhados são mapeados de maneira semelhante a objetos não aninhados. Basta utilizar como tipo de dados object e definir as propriedades. Esta abordagem funciona de forma recursiva.

Para saber mais, acesse:

https://www.elastic.co/guide/en/elasticsearch/guide/current/complex-core-fields.html

---

Stemmer => tranforma a palavra em sua forma mais primitiva, como por exemplo, remove plurais, conjugações e etc.

---

Criar novo indice

PUT /indice_com_sinonimo
{
  "settings": {
    "index": {
      "number_of_shards": 3,
      "number_of_replicas": 0
    },
    "analysis": {
      "filter": {
        "filtro_de_sinonimos": {
            "type": "synonym",
            "synonyms": [
                "esporte,futebol,society,futeba,pelada"
            ]
        }
      },
      "analyzer": {
        "sinonimos": {
          "tokenizer":  "standard",
          "filter": [
            "lowercase",
            "filtro_de_sinonimos"
          ]
        }
      }
    }
  }
}

response:


{
  "acknowledged": true
}

---

verificar os tokens marcados na position 4:

GET /indice_com_sinonimo/_analyze?analyzer=sinonimos&text=eu+gosto+de+jogar+society

GET /indice_com_sinonimo/_analyze?analyzer=sinonimos&text=eu+gosto+de+praticar+esporte

GET /indice_com_sinonimo/_analyze?analyzer=sinonimos&text=arvore+praticamente+pelada

---

PUT /indice_com_sinonimo_2
{
  "settings": {
    "index": {
      "number_of_shards": 3,
      "number_of_replicas": 0
    },
    "analysis": {
      "filter": {
        "filtro_de_sinonimos": {
            "type": "synonym",
            "synonyms": [
        "futebol => futebol,society",
        "society => society,futebol",
        "esporte => esporte,futebol,society,volei,basquete"
            ]
        }
      },
      "analyzer": {
        "sinonimos": {
          "tokenizer":  "standard",
          "filter": [
            "lowercase",
            "filtro_de_sinonimos"
          ]
        }
      }
    }
  }
}

response:

{
  "acknowledged": true
}

---

GET /indice_com_sinonimo_2/_analyze?analyzer=sinonimos&text=futebol

---
O ANALIZER DEVE SER APLICADO TANTO QUANDO INDEXAMOS O DOCUMENTO, QUANTO QUANDO REALIZAMOS A BUSCA

---

Como vimos neste capítulo, podemos definir sinônimos diretamente no atributo synonyms do filtro que definimos. Podemos também fazer uso do atributo synonyms_path para indicar o arquivo de onde os sinônimos serão lidos. O caminho do arquivo deve ser ou relativo ao diretório de configuração (config) do Elasticsearch ou um caminho absoluto para o arquivo.

VER OPINIÃO DO INSTRUTOR


https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-synonym-tokenfilter.html

---

É razoável afirmar que todos nós, uma vez na vida, já recebemos sugestões qual fazemos busca no Google como "Você quis dizer…?". E em geral, quando recebemos esta sugestão, cometemos algum erro de digitação. ElasticSearch também dá suporte a tal tipo de sugestão através da busca Fuzzy.

Na prática, este tipo de busca não é usada para retornar documentos automaticamente, mas sim para dar sugestões aos usuários do que eles realmente estariam procurando.

Para saber mais detalhes, acesse o link a seguir:

https://www.elastic.co/guide/en/elasticsearch/guide/current/fuzzy-matching.html

---

Usos mais avançados para a _bulk API
Para mais detalhes sobre a _bulk API, acesse o link:

https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html

---

Para contar a quantidade de registros, utilizamos o seguinte request:

GET /pessoas/registros/_count
{}

---

Como você deve ter notado, quando utilizamos a Discover Tab e fizemos a busca por matemática ou esportes, tivemos os termos encontrados mostrados em destaque. Esta é uma funcionalidade provida pelo ElasticSearch e não pelo Kibana, e pode ser utilizada em qualquer website.

VER OPINIÃO DO INSTRUTOR
Opinião do instrutor

Para saber mais, acesse o link:

https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-highlighting.html

---


---


---


---


---


---


---
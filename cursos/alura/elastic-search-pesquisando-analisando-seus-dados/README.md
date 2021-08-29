# Elasticsearch: Pesquisando e analisando os seus dados

## Como instalar o Elastic Search Local?

#### Rodar
Acessar o diretório `/bin` do elastic search e executar o arquivo `elasticsearch` de acordo com o sistema operacional.

No caso do Mac:

```shell
./elasticsearch
```

E deve ter uma saída similar a essa em caso de sucesso.

```shell
[2021-08-12 22:04:50,111][INFO ][node                     ] [Electron] version[2.3.1], pid[81083], build[bd98092/2016-04-04T12:25:05Z]
[2021-08-12 22:04:50,112][INFO ][node                     ] [Electron] initializing ...
[2021-08-12 22:04:50,496][INFO ][plugins                  ] [Electron] modules [reindex, lang-expression, lang-groovy], plugins [], sites []
[2021-08-12 22:04:50,517][INFO ][env                      ] [Electron] using [1] data paths, mounts [[/System/Volumes/Data (/dev/disk3s5)]], net usable_space [91.2gb], net total_space [228.2gb], spins? [unknown], types [apfs]
[2021-08-12 22:04:50,517][INFO ][env                      ] [Electron] heap size [1gb], compressed ordinary object pointers [unknown]
[2021-08-12 22:04:50,518][WARN ][env                      ] [Electron] max file descriptors [10240] for elasticsearch process likely too low, consider increasing to at least [65536]
[2021-08-12 22:04:51,626][INFO ][node                     ] [Electron] initialized
[2021-08-12 22:04:51,626][INFO ][node                     ] [Electron] starting ...
[2021-08-12 22:04:51,708][INFO ][transport                ] [Electron] publish_address {127.0.0.1:9300}, bound_addresses {[fe80::1]:9300}, {[::1]:9300}, {127.0.0.1:9300}
[2021-08-12 22:04:51,711][INFO ][discovery                ] [Electron] elasticsearch/0uk6ATeURBiR3DU8n12ogQ
[2021-08-12 22:04:54,754][INFO ][cluster.service          ] [Electron] new_master {Electron}{0uk6ATeURBiR3DU8n12ogQ}{127.0.0.1}{127.0.0.1:9300}, reason: zen-disco-join(elected_as_master, [0] joins received)
[2021-08-12 22:04:54,776][INFO ][http                     ] [Electron] publish_address {127.0.0.1:9200}, bound_addresses {[fe80::1]:9200}, {[::1]:9200}, {127.0.0.1:9200}
[2021-08-12 22:04:54,777][INFO ][node                     ] [Electron] started
[2021-08-12 22:04:54,832][INFO ][gateway                  ] [Electron] recovered [0] indices into cluster_state
```


#### Testar

Basta acessar o endereço em que o Elastic Search sobe.

[http://localhost:9200](http://localhost:9200)


## HTTP

Toda interação com o Elastic Search é feita via protocolo HTTP.

Ou seja, para realizar cadastros, consultas, alterações e etc, serão utilizados os verbos HTTP.


## Kopf

Kopf é um plulgin para o Elasticsearch que disponibiliza um client http para interagit com o banco de dados, além de fornecer dados sobre a saúde do Elasticsearch.

Para instalá-lo, basta:
- Descompactar o arquivo zipado.
- Renomear o diretório apenas para "kopf"
- Mover o diretório koft para o diretório "plugins" dentro do doretório do elasticsearch

OBS: O plugin é disponibilizado com o nome da pasta que foi criado


#### Testar

Assim que o Elasticsearch sobre com o plugin, é disponibilizado um endereço para acessar o Kopf.

[http://localhost:9200/_plugin/kopf](http://localhost:9200/_plugin/kopf)




ElasticSearch não é a única solução disponível que trás o Lucene para a nuvem. É natural que a própria Apache Foundation tenha sua própria solução, afinal, ela é a casa do Lucene.

A solução da Apache tem o nome de Apache Solr. Solr possui um abordagem semelhante que também foca em interoperabilidade e ainda suporta outros tipos de formatos como CSV e XML que não são suportados nativamente pelo ElasticSearch. Contudo, Solr não é muito flexível em relação a extensões e não possui tolerância a falhas nativamente, já que o suporte é dado via SolrCloud.

VER OPINIÃO DO INSTRUTOR
Opinião do instrutor

Para saber mais sobre as diferenças entre ElasticSearch e Solr, visite a página:

http://solr-vs-elasticsearch.com/



---


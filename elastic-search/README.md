# Elastic Seach

O Elastic Search foi construído em Java, com base no Apache Lucene.

O Apache Lucene é uma biblioteca Java construída para armazenar grandes quantidades de dados e oferecer **buscas rápidas**.

Mas o Elastic Search se destaca por:
- Oferecer integração via RESR
- Trabalhar com JSON

Então o Elastic Search fornece um grande poder de busca, podendo trabalhar em nuvem e fornece **data analitics**, como se fosse group by do SQL.

Embora o Elastic Search seja Open Source, há uma empresa por trás do software, a Elastic que fornce serviços como hospedagem, entre outros.


|-------------------|---------------|---------------------------------------------------|
| Banco Relacional  | Elasticsearch | Explicação                                        |
|-------------------|---------------|---------------------------------------------------|
| Instância (Banco) | Index         | Banco de dados                                    |
| Tabela            | Type          | Tabela                                            |
| Schema            | Mapping       | Estrutura de colunas e tipos de dados das colunas |
| Tupla (Linha)     | Documento     | Registro                                          |
| Coluna            | Atributo      | Coluna                                            |
|-------------------|---------------|---------------------------------------------------|

URI => Identificado de recurso único

No elastic serach o conjunto Index/Typo/Identificador é único em todo o elasticsearch, independente do índice.


## Versão

O Elasticsearch trabalha com versões para os documentos armazenados.

A primeira versão sempre será 1, e esse número aumente de 1 em 1 a cada alteração no documento.

Ao realizar uma consulta, por padrão, o Elasticsearch sempre irá retornar a última versão do documento.

Mas é possível solicitar o retorno de uma versão específica do documento.


## Shards

Tradução literal de shard seria "caco".

No Elasticsearch "shard" significa particionar o index.

Assim conseguimos distribuir os dados de um índice em máquinas diferentes.


### Shard Primária

Toda nova escrita no Elasticsearch é realizada na shard primárica.


### Réplicas

Cada shard também pode conter N réplicas.

Assim, caso a maquina onde está a réplica primárica venha a ficar indisponível, uma réplica pode assumir sua posição e disponibilizar os dados novamente.


### Shard Secundária

Assim que as dados são gravados nas shards primárias, eles são replicados para as shards secundárias.

A shards secundárias também fornecem leitura dos dados ao receber as consultas.

Além de que ter shards secundárias possibilita ter informações distribuídas.


### Considerar ao criar shards

Como definir a quantidade de shards?

Estipular o tamanho (em GB) do índice, e assim definir o tamano de shards.

Por exemplo:
Indice: 100GB
Tamanho por shard: 20GB
Quantidade de shards: 5

Uma observação **muito importante** é que muitas shards pode impactar no desempenho de leitura dos dados.

É sabido que shards não devem exceder 50GB.

O problema de ter apenas uma shard é que ocorrerá concorrência, pois a mesma estará sofrendo cadastros e consultas.


### Fine Tunning

Ajustes fino nas queries, para diminuir o tempo de resposta das requisições de busca.


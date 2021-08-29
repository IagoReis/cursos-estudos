

#### Template

<VERBO> <URI>
{
    CONTEÚDO DA REQUISIÇÃO
}

#### Exemplo

POST /catalogo/pessoas
{
    "nome": "João Silva",
    "interesses": ["futebol", "música", "literatura"],
    "cidade": "São Paulo",
    "formacao": "Letras",
    "estado": "SP",
    "pais": "Brasil"
}

#### Resposta

```shell
{
  "_index": "catalogo",
  "_type": "pessoas",
  "_id": "AXs9IdjewFIay2y8eTg7",
  "_version": 1,
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "created": true
}
```


## Criar documento


O Elasticsearch cria uma atributo chamado **_all** para todo documento.

Assim é possível realizar buscas filtrando o valor de todos os atributo, sem a necessidade de definir qual atributo será filtrado.

**Exemplo:**

Vamos supor que temos o documento:

```shell
{
    "nome": "João Silva",
    "interesses": ["futebol", "música", "literatura"],
    "cidade": "São Paulo",
    "formacao": "Letras",
    "estado": "SP",
    "pais": "Brasil"
}
```

Ao salvar este documento, o Elasticsearch indexa o campo **_all** e seu valor será a concatenação dos valores de todos os atributos.

Logo para o documento acima, o campo **_all** será :

`João Silva futebol música literatura São Paulo Letras SP Brasil`

E ao realizarmos uma busca filtrando por algum valor sem informar o campo explicitamente. O Elasticsearch implicitamente irá realizar a busca no campo **_all**.
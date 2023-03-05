```shell
echo "Estou de Redis!"
```

```shell
set "total_de_cursos" 105
get "total_de_cursos"
```

```shell
set "total_de_respostas" 1446104
get "total_de_respostas"

set "total_de_respostas" 1446105
get "total_de_respostas"
```

```shell
set "ultimo_usuario_que_se_logou" "Iago Reis"
get "ultimo_usuario_que_se_logou"
del "ultimo_usuario_que_se_logou"
```



Neste capítulo vimos uma introdução ao Redis. Descreva com suas palavras o que é o Redis.


Redis é uma base de dados não relacional que serve para armazenar dados para serem retornados de forma rápida

Redis é um banco de dados que armazena os dados na forma de chave-valor. Podemos armazenar certos dados, que para serem obtidos em um banco sql, seria necessário varrer todo o banco, como por exemplo, saber o número de alunos cadastrados no Alura. Quando utilizamos o Redis, podemos definir uma chave associada a um valor(o número de alunos). Dessa forma podemos obter o valor de uma forma muito rápida.

Os valores não precisam ser apenas números. Podem ser palavras, listas, conjuntos, entre outros. A medida que avançarmos no curso veremos alguns desses valores.


```shell
set "ultimo_sorteio" "2, 15, 18, 30, 35, 42"
get "ultimo_sorteio"
```


```shell
keys *
```

```shell

```

```shell

```

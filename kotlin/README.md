## Variáveis

### Declaração e inicialização

O Kotlin não permite que nenhuma variável fique sem valor de inicialização, portanto, para compilar o código e rodar, todas as variáveis devem ser inicializadas.

No Kotlin existe a técnica conhecida como inferência de tipo que é quando o compilador interpreta o valor que está sendo atribuído para a variável e determina qual é o seu tipo implicitamente.


### var

Instanciar uma variável com **var** indica que a variável será mutável, ou seja, poderá receber novos valores além do valor inicial.

#### Exemplo

```shell
var nome = "Mario"
nome = "Luigi"
```


### val

Instanciar uma variável com **val** indica que a variável será imutável, ou seja, **não** poderá receber novos valores além do valor inicial.


---


## String

### Concatenação

O Kotlin possui concatenação de strings, podeno ser realizados pelo sinal de mais `+`.

#### Exemplo

```shell
var nome1 = "Mario"
var nome2 = "Luigi"
print(nome1 + " e " + nome2 + " são irmãos")
```

Mas ao se trabalhar com Kotlin, há prefererência de utilizar **template** invés de concatenação.


### String template

Templates substituem a concatenação de strings. Pois utiliza-se apenas uma string e, dentro dela identificamos as variáveis com um cifrão no início da palavra.

#### Exemplo

```shell
var nome1 = "Mario"
var nome2 = "Luigi"
print("$nome1 e $nome2 são irmãos")
```


---


## Controle de Fluxo


### Estrutura de condição


#### IF

##### Exemplo

```shell
var idade = 25
if (idade >= 18) {
    println("Maior de idade")
}
```


#### ELSE

##### Exemplo

```shell
var idade = 25
if (idade >= 18) {
    println("Maior de idade")
}
else {
    println("Menor de idade")
}
```


#### WHEN (switch case)


Uma estrutura de condição utilizando if else.

##### Exemplo

```shell
var saldo: Double = 0.0

if (saldo > 0.0) {
    println("O saldo da conta está positivo")
}
else if (saldo == 0.0) {
    println("O saldo da conta está zerado")
}
else {
    println("O saldo da conta está negativo")
}
```


Mesma estrutura de condição utilizando when.

##### Exemplo

```shell
var saldo: Double = 0.0

when {
    saldo > 0.0 -> {
        println("O saldo da conta está positivo")
    }
    saldo == 0.0 -> {
        println("O saldo da conta está zerado")
    }
    else -> {
        println("O saldo da conta está negativo")
    }
}
```


Simplificando when ao remover chaves (escopo) quando o bloco de código possui apenas uma linha.

##### Exemplo

```shell
var saldo: Double = 0.0

when {
    saldo > 0.0 -> println("O saldo da conta está positivo")
    saldo == 0.0 -> println("O saldo da conta está zerado")
    else -> println("O saldo da conta está negativo")
}
```


#### FOR


##### Exemplo

```shell
for (i in 0..5) {
    println(i)
}

0
1
2
3
4
5
```


##### Exemplo

```shell
for (i in 0..5 step 2) {
    println(i)
}

0
2
4
```


##### Exemplo

```shell
for (i in 0..5) println(i)

0
1
2
3
4
5
```


##### Exemplo

```shell
for (i in 5 downTo 0) {
    println(i)
}

5
4
3
2
1
0
```


##### Exemplo

```shell
for (i in 5 downTo 0 step 2) {
    println(i)
}

5
3
1
```


##### Exemplo

```shell
for (i in 5 downTo 1) println(i)

5
4
3
2
1
0
```


##### Exemplo

```shell
loopPai@ for (i in 1..100 step 2) {
    println("i => $i")
    for (j in 1..100 step 2) {
        println("j => $j")
        if (j == 5) break@loopPai
    }
}
```


#### WHILE

```shell
var i = 1
while (i <= 3) {
    println(i)
    i++
}

1
2
3
```


#### DO WHILE

```shell
var i = 1
do {
    println(i)
    i++
}
while (i <= 3)

1
2
3
```



https://kotlinlang.org/
https://kotlinlang.org/docs/home.html
https://khan.github.io/kotlin-for-python-developers/#primitive-data-types-and-their-limitations
https://kotlinlang.org/docs/properties.html#declaring-properties
https://kotlinlang.org/docs/visibility-modifiers.html
https://kotlinlang.org/docs/functions.html#named-arguments
https://kotlinlang.org/docs/coding-conventions.html#idiomatic-use-of-language-features



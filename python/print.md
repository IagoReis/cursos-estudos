## Print

```
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
(END)
```

**Exemplo**
```
print("Olá mundo!")
Olá mundo!
```

### Alguns argumentos 

### Value

**value** é o valor que queremos imprimir, as reticências indicam que a função pode receber mais de um valor, basta separá-los por vírgula.

### Sep

**sep** é o separador entre os valores, por padrão o separador é um espaço em branco.

**Exemplo**
```
>>> print("Brasil", "ganhou", 5, "titulos mundiais", sep="-")
Brasil-ganhou-5-titulos mundiais
```

### End

**end** é o que acontecerá ao final da função, por padrão há uma quebra de linha, uma nova linha (\n).

**Exemplo**
```
>>> print("Brasil", "ganhou", 5, "titulos mundiais", end="")
Brasil ganhou 5 titulos mundiais>>>
```
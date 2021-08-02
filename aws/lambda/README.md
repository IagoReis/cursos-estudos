# AWS Lambda


## Comando via AWS CLI

### Zipar arquivo do projeto

#### Template

```
zip <NOME>.zip <ARQUIVO>
```

#### Exemplo

```
zip lambda_function.zip lambda_function.py
```


### Deploy da função lambda em formato zio

#### Template

```
aws lambda update-function-code --function-name <NOME-FUNCAO-LAMBDA> --zip-file fileb://<ARQUIVO-ZIP-MAQUINA-LOCAL>
```

#### Exemplo

```
aws lambda update-function-code --function-name analiseSeguranca --zip-file fileb://lambda_function.zip
```


### Gerar uma nova versão da função lambda

#### Template

```
aws lambda publish-version --function-name <NOME-FUNCAO-LAMBDA>
```

#### Exemplo

```
aws lambda publish-version --function-name analiseSeguranca
```


### Criar alias para a função lambda

#### Template

```
aws lambda create-alias --function-name <NOME-FUNCAO-LAMBDA> --function-version <NUMERO-VERSAO> --name <NOME-ALIAS>
```

#### Exemplo

```
aws lambda create-alias --function-name analiseSeguranca --function-version 3 --name prod
```

> **OBS:** os trigerrs não se repetem por versão / alias

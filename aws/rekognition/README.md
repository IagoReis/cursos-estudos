# Rekognition

## Comando via AWS CLI


### Criar collection

#### Template

```
aws rekognition create-collection --collection-id <ID-NOME-DA-COLLECTION>
```

#### Exemplo

```
aws rekognition create-collection --collection-id faces-natal-1990
```


### Excluir collection

#### Template

```
aws rekognition delete-collection --collection-id <ID-DA-COLLECTION>
```

#### Exemplo

```
aws rekognition delete-collection --collection-id faces-natal-1990
```


### Listar collections existentes

#### Exemplo

```
aws rekognition list-collections
```


### Listar conteúdo da collection

Com a opção list-faces, é possível obter uma lista das imagens previamente indexadas. Uma dica é utilizar o grep para filtrar sua saída.

#### Template

```
aws rekognition list-faces --collection-id <ID-DA-COLLECTION>
```

#### Exemplo

```
aws rekognition list-faces --collection-id faces-natal-1990
```

#### Exemplo com grep por ExternalImageId

```
aws rekognition list-faces --collection-id faces-natal-1990 | grep ExternalImageId
```


### Excluir conteúdo da collection

#### Template

```
collection="<ID-DA-COLLECTION>"
aws rekognition delete-faces --collection-id $collection --face-ids $(aws rekognition list-faces --collection-id $collection | grep FaceId | awk -F\" '{print $4}' | xargs)
```

#### Exemplo

```
collection="faces-natal-1990"
aws rekognition delete-faces --collection-id $collection --face-ids $(aws rekognition list-faces --collection-id $collection | grep FaceId | awk -F\" '{print $4}' | xargs)
```

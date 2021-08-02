# S3 - Simple Storage Service

## Comando via AWS CLI

### Enviar imagem para o S3

#### Template

```
aws s3 cp <ARQUIVO> s3://<NOME-BUCKET-S3>
```

#### Exemplo

```
aws s3 cp foto.png s3://bucket_fotos
```

### Sync

Através de comando sync, é possível realizar multiplos uploads

#### Template

```
aws s3 sync . s3://<NOME-BUCKET-S3>
```

#### Exemplo

```
aws s3 sync . s3://bucket-alura-1-3
```


aws s3 rm s3://bucket-alura-1-3 --recursive



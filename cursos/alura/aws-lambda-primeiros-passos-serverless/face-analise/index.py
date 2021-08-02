import boto3

s3 = boto3.resource('s3')
client = boto3.client('rekognition')

s3_bucket_repo = 'bucket-alura-1-3'
rekognition_collection_id = 'faces-got'


def listar_imagens():
    imagens = []
    bucket = s3.Bucket(s3_bucket_repo)
    for imagem in bucket.objects.all():
        imagens.append(imagem.key)
    print(imagens)
    return imagens


def indexar_colecao(imagens):
    for i in imagens:
        print("Indexando {}".format(i))
        response = client.index_faces(
            CollectionId=rekognition_collection_id,
            ExternalImageId=i,
            Image={
                'S3Object': {
                    'Bucket': s3_bucket_repo,
                    'Name': i
                }
            }
        )
        print("{} indexado com sucesso".format(i))


if __name__ == '__main__':
    imagens = listar_imagens()
    indexar_colecao(imagens)

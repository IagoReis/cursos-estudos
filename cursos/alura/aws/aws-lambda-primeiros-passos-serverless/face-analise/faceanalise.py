import boto3
import json

s3 = boto3.resource('s3')
client = boto3.client('rekognition')

s3_bucket_repo = 'bucket-alura-1-3'
rekognition_collection_id = 'faces-got'
s3_bucket_site = 'alura-reko-site'


def detectar_faces(imagem):
    faces_detectadas = client.index_faces(
        CollectionId=rekognition_collection_id,
        ExternalImageId='TEMPORARIA',
        Image={
            'S3Object': {
                'Bucket': s3_bucket_repo,
                'Name': imagem
            }
        }
    )
    return faces_detectadas


def listar_face_ids_detectadas(faces_detectadas):
    face_id = []
    for i in range(len(faces_detectadas['FaceRecords'])):
        face_id.append(faces_detectadas['FaceRecords'][i]['Face']['FaceId'])
    return face_id


def comparar_imagens(ids):
    resultado_comparacao = []
    for i in ids:
        resultado_comparacao.append(
            client.search_faces(
                CollectionId=rekognition_collection_id,
                FaceId=i,
                FaceMatchThreshold=50,
                MaxFaces=10
            )
        )
    return resultado_comparacao


def gerar_dados_json(comparacao):
    dados_json = []
    for face_encontrada in comparacao:
        if(len(face_encontrada.get('FaceMatches')) > 0):
            perfil = dict(
                nome=face_encontrada.get('FaceMatches')[0].get('Face').get('ExternalImageId'),
                similaridade=round(face_encontrada.get('FaceMatches')[0].get('Similarity'), 2)
            )
            dados_json.append(perfil)
    return dados_json


def publicar_dados_json(dados_json):
    arquivo = s3.Object(s3_bucket_site, 'dados.json')
    arquivo.put(Body=json.dumps(dados_json, indent=2))


def excluir_face(faces_ids):
    client.delete_faces(
        CollectionId=rekognition_collection_id,
        FaceIds=faces_ids
    )


def excluir_imagem(imagem):
    s3.Object(s3_bucket_repo, imagem).delete()


def main(event, context):
    imagem = event["Records"][0]["s3"]["object"]["key"]
    print("Processando imagem {}".format(imagem))
    faces_detectadas = detectar_faces(imagem)
    ids = listar_face_ids_detectadas(faces_detectadas)
    comparacao = comparar_imagens(ids)
    dados_json = gerar_dados_json(comparacao)
    publicar_dados_json(dados_json)
    excluir_face(ids)
    excluir_imagem(imagem)
    print(json.dumps(dados_json, indent=2))


if __name__ == "__main__":
    main()
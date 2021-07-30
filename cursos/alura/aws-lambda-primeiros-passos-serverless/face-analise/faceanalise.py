import boto3
import json

s3 = boto3.resource('s3')
client = boto3.client('rekognition')

s3_bucket_repo = 'bucket-alura-1-3';
rekognition_collection_id = 'faces-naruto'


def detectar_faces():
    faces_detectadas = client.index_faces(
        CollectionId=rekognition_collection_id,
        ExternalImageId='TEMPORARIA',
        Image={
            'S3Object': {
                'Bucket': s3_bucket_repo,
                'Name': '_analise.png'
            }
        }
    )
    return faces_detectadas


if __name__ == "__main__":
    faces_detectadas = detectar_faces()
    print(json.dumps(faces_detectadas, indent=4))
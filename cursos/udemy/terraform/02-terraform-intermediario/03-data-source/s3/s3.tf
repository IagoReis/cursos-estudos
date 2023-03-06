resource "random_pet" "random_bucket_name" {
  length = 3
}

resource "aws_s3_bucket" "bucket" {
  bucket = random_pet.random_bucket_name.id
}

resource "aws_s3_bucket_object" "object" {
  bucket       = aws_s3_bucket.bucket.bucket
  source       = "output.json"
  key          = "instances/instances-${local.instance.ami}.txt"
  etag         = filemd5("output.json")
  content_type = "application/json"
}
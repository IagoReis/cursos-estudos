resource "aws_s3_bucket" "bucket" {
  bucket = "${random_pet.bucket.id}-${var.environment}"
  acl    = "private"
  tags   = local.commons_tags
}

resource "aws_s3_bucket" "bucket_imported" {
  bucket = "bucket-teste-curso-udemy"
  acl    = "private"
  tags = {
    Imported = "2022-03-05"
  }
}

resource "aws_s3_bucket_object" "name" {
  bucket       = aws_s3_bucket.bucket.bucket
  source       = local.ip_file_path
  key          = "config/${local.ip_file_path}"
  content_type = "application/json"
  etag         = filemd5(local.ip_file_path)
  tags         = local.commons_tags
}

resource "aws_s3_bucket_object" "random" {
  bucket       = aws_s3_bucket.bucket.bucket
  source       = local.ip_file_path
  key          = "config/${random_pet.bucket.id}.json"
  content_type = "application/json"
  etag         = filemd5(local.ip_file_path)
  tags         = local.commons_tags
}
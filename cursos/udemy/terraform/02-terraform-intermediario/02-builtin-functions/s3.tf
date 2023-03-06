resource "random_pet" "random_bucket_name" {
  length = 5
}

resource "aws_s3_bucket" "bucket" {
  bucket = "${random_pet.random_bucket_name.id}-${var.environment}"
  tags   = local.commons_tags
}

resource "aws_s3_bucket_object" "bucket_object" {
  bucket       = aws_s3_bucket.bucket.bucket
  key          = "${uuid()}.${local.file_ext}"
  source       = data.archive_file.json.output_path
  etag         = filemd5(data.archive_file.json.output_path)
  content_type = "application/zip"
  tags         = local.commons_tags
}

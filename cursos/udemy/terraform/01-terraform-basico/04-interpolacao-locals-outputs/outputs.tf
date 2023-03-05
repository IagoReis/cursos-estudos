output "bucket_name" {
  value = aws_s3_bucket.bucket.bucket
}

output "bucket_arn" {
  value = aws_s3_bucket.bucket.arn
}

output "ips_file_path" {
  value = "s3://${aws_s3_bucket.bucket.bucket}/${aws_s3_bucket_object.name.key}"
}

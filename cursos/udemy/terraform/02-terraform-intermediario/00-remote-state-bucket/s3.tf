data "aws_caller_identity" "current" {}

resource "aws_s3_bucket" "bucket_remote_state" {

  bucket = "tfstate-${data.aws_caller_identity.current.account_id}"

  versioning {
    enabled = true
  }

}

output "remote_state_bucket_name" {
  value = aws_s3_bucket.bucket_remote_state.bucket
}

output "remote_state_bucket_arn" {
  value = aws_s3_bucket.bucket_remote_state.arn
}

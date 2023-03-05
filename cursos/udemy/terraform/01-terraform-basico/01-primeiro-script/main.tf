terraform {
  required_version = "0.14.4"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "3.23.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "bucket" {

  bucket = "my-tf-test-bucket-51651215581165009055515"
  acl    = "private"

  tags = {
    "key" = "value"
  }

}

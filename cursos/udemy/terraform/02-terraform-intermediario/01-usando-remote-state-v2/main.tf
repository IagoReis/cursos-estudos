terraform {
  required_version = "0.14.4"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "3.23.0"
    }
  }

  backend "s3" {}
}

provider "aws" {
  region  = var.aws_region
  profile = var.aws_profile
}

#terraform init -backend=true -backend-config="bucket=tfstate-904234446955" -backend-config="key=dev/01-usando-remote-state/terraform.tfstate" -backend-config="region=us-east-1" -backend-config="profile=default"
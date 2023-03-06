terraform {

  required_version = "0.14.4"

  required_providers {

    aws = {
      source  = "hashicorp/aws"
      version = "3.23.0"
    }

    random = {
      source  = "hashicorp/random"
      version = "3.0.1"
    }

    archive = {
      source  = "hashicorp/archive"
      version = "2.0.0"
    }

    template = {
      source  = "hashicorp/template"
      version = "2.2.0"
    }
  }

  backend "s3" {
    bucket = "tfstate-904234446955"
    key    = "dev/02-builtin-functions/terraform.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region  = var.aws_region
  profile = var.aws_profile
}

#terraform init -backend=true -backend-config="backend.hcl"

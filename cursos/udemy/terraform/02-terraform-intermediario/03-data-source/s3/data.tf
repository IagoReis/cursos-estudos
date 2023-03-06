data "terraform_remote_state" "server" {

  backend = "s3"

  config = {
    bucket = "tfstate-904234446955"
    key    = "dev/03-data-source/terraform.tfstate"
    region = var.aws_region
  }
}

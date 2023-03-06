locals {

  instance_number = lookup(var.instance_number, var.environment)

  instance_ami = var.instance_ami

  instance_type = lookup(var.instance_type, var.environment)

  file_ext = "zip"

  object_name = "arquivo-gerado-com-template"

  commons_tags = {
    ManagedBy = "Terraform"
    Owner     = "Iago Reis"
    Year      = 2023
  }
}
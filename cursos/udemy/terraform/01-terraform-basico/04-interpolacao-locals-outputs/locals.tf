locals {
  commons_tags = {
    ManagedBy   = "Terraform"
    Environment = var.environment
    Owner       = "Iago Reis"
  }

  ip_file_path = "ips.json"
}

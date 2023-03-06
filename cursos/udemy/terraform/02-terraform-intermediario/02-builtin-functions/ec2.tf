resource "aws_instance" "ec2_instance" {

  count         = local.instance_number <= 0 ? 0 : local.instance_number
  ami           = local.instance_ami
  instance_type = local.instance_type

  tags = merge(
    local.commons_tags,
    {
      Project     = "Curso Terraform para AWS"
      Environment = format("%s", var.environment)
      Name        = format("Instance %d", count.index + 1)
    }
  )
}

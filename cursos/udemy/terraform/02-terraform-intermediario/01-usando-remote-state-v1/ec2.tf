resource "aws_instance" "ec2_instance" {
  ami           = var.instance_ami
  instance_type = var.instance_type
}
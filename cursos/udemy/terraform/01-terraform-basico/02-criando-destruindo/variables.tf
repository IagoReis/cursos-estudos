variable "aws_region" {
  type = string
  description = ""
  default = "us-east-1"
}

variable "aws_profile" {
  type = string
  description = ""
  default = "default"
}

variable "instance_ami" {
  type = string
  description = ""
  default = "ami-006dcf34c09e50022"
}

variable "instance_type" {
  type = string
  description = ""
  default = "t3.micro"
}

variable "instance_tags" {
  type = map(string)
  description = ""
  default = {
    Name = "Ubuntu"
    Teste = "True"
    Curso = "Udemy"
  }
}

variable "variavel_obrigatoria" {
  type = string
  description = "Teste de variável obrigatória"
}

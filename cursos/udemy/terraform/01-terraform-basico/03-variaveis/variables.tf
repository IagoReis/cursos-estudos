
variable "environment" {
  type        = string
  description = "Ambiente em que será executado"
}

variable "aws_region" {
  type        = string
  description = ""
}

variable "aws_profile" {
  type        = string
  description = ""
}

variable "instance_ami" {
  type        = string
  description = ""
}

variable "instance_type" {
  type        = string
  description = ""
}

variable "instance_tags" {
  type        = map(string)
  description = ""
}

variable "variavel_obrigatoria" {
  type        = string
  description = "Teste de variável obrigatória"
}

variable "aws_region" {
  type        = string
  description = ""
  default     = "us-east-1"
}

variable "aws_profile" {
  type        = string
  description = ""
  default     = "default"
}

variable "instance_ami" {
  type        = string
  description = "AMI da instância EC2"
}

variable "instance_type" {
  type        = string
  description = ""
  default     = "t3.micro"
}

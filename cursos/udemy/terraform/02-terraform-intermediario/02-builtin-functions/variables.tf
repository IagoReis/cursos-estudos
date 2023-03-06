variable "environment" {
  type        = string
  description = ""
}

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
  default     = "ami-006dcf34c09e50022"

  validation {
    condition     = length(var.instance_ami) > 4 && substr(var.instance_ami, 0, 4) == "ami-"
    error_message = "The instance_ami value must be a valid AMI id, stating with \"ami-\"."
  }
}

variable "instance_number" {

  type = object(
    {
      dev  = number
      prod = number
    }
  )

  description = "Number of instances to create"

  default = {
    dev  = 1
    prod = 3
  }
}

variable "instance_type" {

  type = object({
    dev  = string
    prod = string
  })

  description = ""

  default = {
    dev  = "t3.micro"
    prod = "t3.micro"
  }
}

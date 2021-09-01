// thanks https://learn.hashicorp.com/tutorials/terraform/aws-build?in=terraform/aws-get-started
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-2"
}

resource "aws_instance" "app_server" {
  ami           = "ami-0a817b0856bd5d87a"
  instance_type = "t2.micro"

  tags = {
    Name = "CoolINstanceByVagrant"
  }
}

terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "≥4.66.0"
    }
  }
}

provider "aws" {
  # Configuration options
  region = "eu-west-2"
  access_key = "my-access-key"
  secret_key = "my-secret-key"
}


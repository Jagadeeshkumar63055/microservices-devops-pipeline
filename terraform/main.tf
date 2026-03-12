terraform {
  required_providers {
    local = {
      source = "hashicorp/local"
      version = "2.4.0"
    }
  }
}

provider "local" {}

resource "local_file" "project_info" {
  filename = "${path.module}/project.txt"
  content  = "Microservices DevOps Platform created using Terraform"
}
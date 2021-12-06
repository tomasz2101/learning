terraform {
    required_providers {
        azurerm = {
            version = "2.80.0"
        }
    }
    backend "azurerm" {
        resource_group_name   = "Learning"
        storage_account_name  = "tstate21404"
        container_name        = "tstate"
        key                   = "terraform.tfstate"
    }
}
provider "azurerm" {
    features {}
}

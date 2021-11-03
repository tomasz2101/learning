output "public_ip_address" {
  value = "${azurerm_public_ip.myterraformpublicip.ip_address}"
}
output "username" {
  value = "${azurerm_linux_virtual_machine.myterraformvm.admin_username}"
}
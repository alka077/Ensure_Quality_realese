resource "azurerm_network_interface" "main" {
  name                = "${var.application_type}-NetworkInterface"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${var.subnet_id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "${var.public_ip}"
  }
}

resource "azurerm_linux_virtual_machine" "" {
  name                = "myLinuxVM"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  size                = "Standard_D2s_v3"
  admin_username      = "devopsagent"
  admin_password      = "DevOpsAgent@123"
  network_interface_ids = [azurerm_network_interface.main.id]
  # admin_ssh_key {
  #   username   = "devopsagent"
  #   public_key = "/home/devopsagent/.ssh/id_rsa"
  # }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "20.04-LTS"
    version   = "latest"
  }
}

resource "proxmox_lxc" "manager1" {
  target_node     = "pve"
  hostname        = "manager1"
  ostemplate      = "local:vztmpl/ubuntu-22.04-standard_22.04-1_amd64.tar.zst"
  password        = "ubuntu"
  unprivileged    = true
  cores           = 2
  memory          = 1024
  start           = true # start after creation
  ssh_public_keys = file("~/.ssh/id_rsa.pub")
  rootfs {
    storage = "local-lvm"
    size    = "8G"
  }
  network {
    name   = "eth0"
    bridge = "vmbr0"
    #ip     = "dhcp"
    ip     = "192.168.1.11/24"
    gw     = "192.168.1.1"
  }
  features {
    nesting = true
  }
}

resource "proxmox_lxc" "worker1" {
  target_node     = "pve"
  hostname        = "worker1"
  ostemplate      = "local:vztmpl/ubuntu-22.04-standard_22.04-1_amd64.tar.zst"
  password        = "ubuntu"
  unprivileged    = true
  cores           = 2
  memory          = 1024
  start           = true # start after creation
  ssh_public_keys = file("~/.ssh/id_rsa.pub")
  rootfs {
    storage = "local-lvm"
    size    = "8G"
  }
  network {
    name   = "eth0"
    bridge = "vmbr0"
    #ip     = "dhcp"
    ip     = "192.168.1.11/24"
    gw     = "192.168.1.1"
  }
  features {
    nesting = true
  }
}

resource "proxmox_lxc" "worker2" {
  target_node     = "pve"
  hostname        = "worker2"
  ostemplate      = "local:vztmpl/ubuntu-22.04-standard_22.04-1_amd64.tar.zst"
  password        = "ubuntu"
  unprivileged    = true
  cores           = 2
  memory          = 1024
  start           = true # start after creation
  ssh_public_keys = file("~/.ssh/id_rsa.pub")
  rootfs {
    storage = "local-lvm"
    size    = "8G"
  }
  network {
    name   = "eth0"
    bridge = "vmbr0"
    #ip     = "dhcp"
    ip     = "192.168.1.13/24"
    gw     = "192.168.1.1"
  }
  features {
    nesting = true
  }
}
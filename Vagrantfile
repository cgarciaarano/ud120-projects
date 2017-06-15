# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
VM_NAME = "udacity-ml"
MEMORY = 1536

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "packer/ubuntu-16.04.2-server-amd64-docker.box"
  config.vm.provision "shell", path: "vagrant_provision.sh"
  config.vm.synced_folder ".", "/vagrant"

  config.vm.provider "virtualbox" do |vb| 
     # Use VBoxManage to customize the VM. For example to change name, memory and DNS resolution:
     vb.name = "#{VM_NAME}"
     vb.customize ["modifyvm", :id, "--memory", "#{MEMORY}"]
       vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  end
end

sudo apt-get update
sudo apt-get install open-vm-tools-desktop -y
sudo apt-get install git -y
git clone https://github.com/galjabari/cloud-computing.git
sh cloud-computing/install-docker.sh
sh cloud-computing/install-portainer.sh
sh cloud-computing/install-vscode.sh

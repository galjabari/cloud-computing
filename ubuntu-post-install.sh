sudo apt-get update
sudo apt-get install open-vm-tools-desktop -y
sudo apt-get install git -y
git clone https://github.com/galjabari/cloud-computing.git
bash cloud-computing/install-docker.sh
bash cloud-computing/install-portainer.sh
bash cloud-computing/install-vscode.sh

# Setup
sudo apt-get install wget gpg
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > p>
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings>
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packa>
rm -f packages.microsoft.gpg
## Install
sudo apt install apt-transport-https
sudo apt update
sudo apt install code # or code-insiders

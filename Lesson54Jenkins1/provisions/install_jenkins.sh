# install java v17
sudo apt update
sudo apt-get upgrade -y
sudo apt install fontconfig git openjdk-17-jre  -y
java -version

# install jenkins
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins -y
# This line allows the jenkins user to run any command (ALL) as any user ((ALL)) without being prompted for a password (NOPASSWD).
# need to add this to sudo file (sudo visudo)  # jenkins ALL=(ALL) NOPASSWD: ALL
# add jenkins to sudo group
sudo usermod -aG sudo jenkins  
sudo usermod -aG vagrant jenkins  
# start jenkins
sudo systemctl start jenkins
# enable jenkins (to start on boot)
sudo systemctl enable jenkins
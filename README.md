# Kali-Docker
Will pull and run a kali vm on your machine with docker

Setup an SSH server

Paste this into the CLI:
`apt update && apt install openssh-server sudo -y && systemctl enable ssh && service ssh start && adduser kali && usermod -aG sudo kali`

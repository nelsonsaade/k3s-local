### ON VM K3S
# Get IP from VM
ip a
ifconfig

# Edit auth login from ssh
sudo vi /etc/ssh/sshd_config

# Press I to edit file and press Esc :wq to save
PasswordAuthentication yes
PermitRootLogin yes

# Restart VM
sudo reboot now

# Login with SSH
ssh rancher@VM-IP

# Change IP Address from node
sudo connmanctl services
sudo connmanctl config <ethernet service> --ipv4 manual <IP Address> <Netmask> <gateway> --nameservers <DNS Address>

# Restart VM
sudo reboot now

# Get kubeconfig
sudo cat /etc/rancher/k3s/k3s.yaml

### ON WSL

# install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client

# Apply kubeconfig

scp rancher@$VM IP:/etc/rancher/k3s/k3s.yaml /home/$USER/k3s.yaml
mkdir -p ~/.kube
mv ~/k3s.yaml ~/.kube/config
chmod 600 ~/.kube/config

# Change IP from 127.0.0.1 to $VM IP
nano ~/.kube/config

# Test connection
kubectl get nodes
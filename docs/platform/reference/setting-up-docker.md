# Set up docker in Ubuntu

## install docker in Ubuntu

1. Set up the repository:

   ```shell
   sudo apt-get update

   sudo apt-get install -y \
      apt-transport-https \
      ca-certificates \
      curl \
      gnupg \
      lsb-release

   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

   echo \
     "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
     $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

2. Install the docker engine. For information on docker engine installation, refer to [Install Docker Engine using the repository](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository):

   ```shell
   sudo apt-get update
   sudo apt-get install -y docker-ce docker-ce-cli containerd.io
   ```

3. Manage the docker as a non-root user:

   ```shell
   sudo groupadd -f docker
   sudo usermod -aG docker $USER
   newgrp docker
   ```

4. Log out and log in to your desktop again.

## Incorporate network setting

Before applying this configuration, ensure your host machine is behind the proxy server and uses special DNS.

### Proxy

1. Create a systemd drop-in directory for the docker service:

   ```shell
   sudo mkdir -p /etc/systemd/system/docker.service.d
   ```

2. Create a file named `/etc/systemd/system/docker.service.d/http-proxy.conf` that adds `PROXY` related environment variables:

   ```conf
   [Service]
   Environment="HTTP_PROXY=http://proxy_ip"
   Environment="HTTPS_PROXY=https://proxy_ip"
   Environment="NO_PROXY=localhost,127.0.0.1"
   ```

3. Restart the docker daemon:

   ```shell
   sudo service docker restart
   ```

4. Verify that the configuration has been loaded and matches the changes you made:

   ```shell
   sudo systemctl show --property=Environment docker
   ```

### DNS

1. Create a file named `/etc/docker/daemon.json` that adds the `dns` key:

   ```json
   {
     "dns": [
       "dns_ip",
       "dns_ip"
     ]
   }
   ```

2. Restart the docker daemon:

   ```shell
   sudo service docker restart
   ```

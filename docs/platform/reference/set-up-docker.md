# Set up docker in Ubuntu

## Install docker in Ubuntu

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

2. Install the docker engine and tools:

   ```shell
   sudo apt-get update
   sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose
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
   Environment="HTTP_PROXY=http://proxy_ip:port"
   Environment="HTTPS_PROXY=https://proxy_ip:port"
   Environment="NO_PROXY=localhost,127.0.0.1,tic"
   ```

3. Restart the docker daemon:

   ```shell
   sudo systemctl daemon-reload
   sudo systemctl restart docker
   ```

4. Verify that the configuration has been loaded and matches the changes you made:

   ```shell
   sudo systemctl show --property=Environment docker
   ```

5. Add proxy configurations to `~/.docker/config.json` file to configure the Docker client:

   ```json
   {
      "proxies": {
         "default": {
            "httpProxy": "http://proxy_ip:port",
            "httpsProxy": "http://proxy_ip:port",
            "noProxy": "localhost,127.0.0.1,tic"
         }
      }
   }
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
   sudo systemctl restart docker
   ```

For more details, please refer the official docker document.
  * [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
  * [Configure Docker to use a proxy server](https://docs.docker.com/network/proxy/)
  * [Configure the daemon with systemd](https://docs.docker.com/config/daemon/systemd/)
  * [Specify DNS servers for Docker](https://docs.docker.com/engine/install/troubleshoot/#specify-dns-servers-for-docker)

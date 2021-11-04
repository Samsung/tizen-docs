# Create Tizen images with Tizen Image Creator (TIC)

This topic provides information on how to create a Tizen image with TIC.

To use TIC, you have to set up the docker initially. For information on docker setup, see [Setting up Docker](../reference/setting-up-docker.md)

## Tizen Image Creator

TIC is an image creator tool used to create images for Tizen. The main features of TIC are as follows:

- Provides web-based user interface
- Easy installation with the docker image
- Supports YAML style recipe

### Supported Environment

- Ubuntu 16.04 LTS or Higher

### Set up TIC on your PC

Install `docker-compose` tool, to use pre-configured docker-compose file to run the TIC service:

```shell
   sudo apt-get install docker-compose
```

Download pre-configured docker-compose file:

- [TIC docker-compose](https://s3-us-west-1.amazonaws.com/tizenschool/257/docker-compose.yaml)

Run the TIC docker container as a service:

```shell
   docker login -u [DockerHub_Username] -p [DockerHub_Password]
   docker-compose pull
   docker-compose up -d
```

### Connect to the TIC web-service

- Open the web browser and enter <http://127.0.0.1:8088> in the address bar. You can see TIC web UI as following image:

  ![TIC web-service](./media/tic-ui.png)

Once the Tizen image is created, the final step is to flash the image to a target device for verification. For more information, see [Flashing an Image to RPI](flashing-rpi.md).

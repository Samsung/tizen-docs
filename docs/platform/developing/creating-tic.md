# Creating Tizen Images with Tizen Image Creator (TIC)

This topic provides information on how to create a Tizen image with TIC.

You have to setting up Docker to use TIC, study the following instructions:

- [Setting up Docker](../reference/setting-up-docker.md)

## Tizen Image Creator

TIC is an image creator that is used to create images for Tizen.

- provides web-based user interface
- easy installation with the docker image
- YAML style recipe is supported

### Supported Environment

- Ubuntu 16.04 LTS or Later

## How to use TIC

### Install docker-compose tool

   ```shell
    sudo apt-get install docker-compose
   ```

### Download docker-compose file for TIC

- [TIC docker-compose](./media/docker-compose.yaml)

## Run the TIC docker container as a service

   ```shell
   docker login -u [DockerHub_Username] -p [DockerHub_Password]
   docker-compose pull
   docker-compose up -d
   ```

## Connect to TIC web-service

- Open any browser with <http://127.0.0.1:8088>

  ![TIC web-service](./media/tic-ui.png)

Once the Tizen image is created, the final step is to flash the image to a target device for verification. For more information, see [Flashing an Image to Device](https://docs.tizen.org/platform/developing/flashing-rpi/).

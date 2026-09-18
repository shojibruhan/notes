```bash
docker build -t myapp:latest .
```

myapp: name of the image

```bash
docker run -it myapp:latest
docker run -it --rm myapp:latest # remove container after exit
```

- -it: interactive mode with a terminal
- -t: allocate a pseudo-TTY
- -d: run container in detached mode

### Check running containers and stop them

```bash
docker ps
# or
docker ps -a
# or long version but no need to remember
docker container ls

docker container ls -a
```

```bash
docker stop <container_id>
```

- ps: list running containers. ps meaning process status
- a: list all containers (running and stopped)

### architecture

docker is a client-server application/architecture with three major components:

- Docker client: The command line tool that allows users to interact with Docker.
- Docker daemon: The background service that manages Docker containers and images. They are like api gateway.
- Docker Containerization: The technology that allows applications to run in isolated environments called containers.
  - namespace: Provides isolation for processes, network
    and filesystem.
  - Control groups (cgroups): Limit and prioritize resource usage (CPU, memory, disk I/O) for containers.

- Docker registry: A repository for storing and distributing Docker images. Like github. Docker Hub is the most popular public registry, but you can also set up your own private registry.
- Docker images: Read-only templates used to create containers.
- Docker containers: Lightweight, portable, and self-sufficient environments that run applications.
- Dockerfile: A text file that contains instructions for building a Docker image.
- Docker Compose: A tool for defining and running multi-container Docker applications using a YAML file.
- Docker Hub: A cloud-based registry service for sharing and managing Docker images.
- Docker Swarm: A native clustering and orchestration tool for managing Docker containers across multiple hosts.
- Docker networking: The system that allows containers to communicate with each other and with the outside world.

Docker clinet communicates with the Docker daemon using REST API over HTTP, over UNIX sockets or a network interface.

The Docker daemon listens for requests from the Docker client and manages the containers, images, networks, and volumes on the host system.

Docker compose is also a client that communicates with the Docker daemon to manage multi-container applications. It uses a YAML file to define the services, networks, and volumes required for the application.

### Process

1. Image Createion: A Docker image is created using a Dockerfile, which contains a set of instructions for building the image. The `docker build` command is used to create an image from the Dockerfile. Docker specifies a base image, copies files, installs dependencies, and sets up the environment for the application.

2. Image building: Docker client sends the Dockerfile to the Docker daemon, which reads the instructions and executes them to build the image. The daemon creates a series of layers, each representing a change made to the image. These layers are cached, allowing for faster builds in subsequent runs.

3. Image Storage for sharing: Once the image is built, it can be stored in a Docker registry, such as Docker Hub or a private registry. The `docker push` command is used to upload the image to the registry, making it available for others to use.

4. Container Lifecycle:
   - Docker client sends a request to the Docker daemon to create a container from the image using the `docker run` command.
   - Daemon checks if the image is available locally; if not, it pulls the image from the registry.
   - The Docker daemon creates a new container based on the image, allocating resources and setting up the necessary namespaces and cgroups for isolation.
5. Container Isolation: The container runs in an isolated environment, with its own filesystem, network interfaces, and process space. The application inside the container can run independently of the host system and other containers.

6. Container Management: The Docker client can be used to manage the container's lifecycle, including starting, stopping, pausing, and removing containers. The `docker ps` command lists running containers, while `docker stop` and `docker rm` are used to stop and remove containers, respectively.

Docker Swarm, Kubernetes and other orchestration tools can be used to manage multiple containers across different hosts, providing features like load balancing, service discovery, and scaling.

### Client Commands

```bash
docker pull <image_name> # pull image from registry
docker push <image_name> # push image to registry
docker run <image_name> # run a container from an image
docker images # list all images
docker rmi <image_name> # remove image
docker logs <container_id> # view container logs
docker exec -it <container_id> <command> # execute command in running container
docker inspect <container_id> # view detailed information about a container
docker stats <container_id> # view resource usage statistics for a container
docker network ls # list all networks
docker network create <network_name> # create a new network
docker network rm <network_name> # remove a network
docker volume ls # list all volumes
docker volume create <volume_name> # create a new volume
docker volume rm <volume_name> # remove a volume
docker-compose up # start services defined in docker-compose.yml
docker-compose down # stop and remove services defined in docker-compose.yml
```

```bash
docker create <container_name> # create a new container without starting it
docker start <container_name> # start a stopped container
docker start -a <container_name> # start a stopped container and attach to it
docker restart <container_name> # restart a running container
docker pause <container_name> # pause a running container
docker unpause <container_name> # unpause a paused container

docker stop <container_name> # stop a running container
docker stop <container_id> # stop a running container
docker kill <container_name> # forcefully stop a running container
```

### Delete all containers and images

```bash
docker system prune
docker system prune -a
```

```bash
docker rmi image_id
docker rm container_id
```

### Example: run redis container

```bash
docker run redis
# or
# docker run -d --name my-redis redis:latest
# open another terminal and run
docker ps # find redis container id
docker exec -it <container_id> redis-cli
# write ping in the redis-cli and press enter, you should see pong as a response 'pong

```

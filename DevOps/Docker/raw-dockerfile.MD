# Dockerfile

A text file with step by step commands.

There are 3 main types of instructions in a Dockerfile:

1. Base image:

```Dockerfile
FROM <image_name>:<tag>
FROM node:14-alpine
```

2. Configuration Commands:

```Dockerfile
WORKDIR /app
COPY package.json .
COPY requirements.txt .

RUN apt-get update && apt-get install -y <package_name>
RUN npm install
RUN npm build # for typescript
RUN pip install -r requirements.txt

COPY . .

EXPOSE 3000
```

3. Startup command:

```Dockerfile

CMD ["node", "app.js"]
CMD ["npm", "start"]
CMD ["python", "app.py"]

```

- `WORKDIR`: where will we put our application files inside the container.
- `COPY`: copies files from the host machine to the container. It can be package.json, requirements.txt, etc. Running first the dependencies installation commands will help to cache the dependencies and avoid re-installing them every time we build the image.

- `RUN`: runs commands inside the container. It can be used to install dependencies, run scripts, etc inside the container/OS.

- `COPY . .`: copies all the files from the current directory on the host machine to the current directory in the container(app from WORKDIR).

  But create `.dockerignore` file to avoid copying unnecessary files like node_modules, .git, etc.

- `EXPOSE`: exposes a port to the host machine. It can be 3000, 5000, etc.

- `CMD`: the command that will be executed when the container starts. It can be node, npm, python, etc. Always take Array as arguments. It is the last command in the Dockerfile. If you want to run multiple commands, you can use `&&` or create a shell script and run it. example:

  ```Dockerfile
  CMD ["sh", "-c", "npm install && npm start"]
  ```

- `RUN` vs `CMD`: `RUN` on build time, `CMD` on run time.

- `ADD`: similar to `COPY`, but it can also copy files from a URL. It is not recommended to use it, as it can lead to unexpected behavior.

```Dockerfile
ADD <source> <destination>
ADD https://example.com/file.txt /app/file.txt
```

- `ENV`: sets environment variables inside the container. It can be used to set configuration values, secrets, etc.

```Dockerfile
ENV <key>=<value>
ENV PORT=3000
```

```bash
docker build -t <image_name>:<tag> .
docker build -t my-app .
```

```bash
docker run -it -p 3000:3000 <image_name>:<tag>
docker run -it -p 3000:3000 --name <container_name> <image_name>:<tag>

docker run -it --rm -p 4001:4000 -e DATABASE_URL=demo_url --name my-app-conn my-app
```

**OR**

**use `docker-compose.yml`**

# Tools

A simple web application that tracks how many times a tool has been visited.

Used mostly for demonstration in various courses and presentations.

It can be used in containers or by following the classical approach.

Contains the following set of files:

```text
.
├── db                        ---> database image files
|   └── db_setup.sql          ---> database seed file
├── web                       ---> web image files
|   ├── config.php            ---> main app config file
|   └── index.php             ---> main app file
├── Dockerfile.db             ---> used to build the database image
├── Dockerfile.web            ---> used to build the web image. Application files should be mounted on start
├── Dockerfile.web.embedded   ---> used to build the web image with embedded application files
├── README.md                 ---> this file
└── tools.png                 ---> sample output of the application
```

Images can be build with the following commands:

```bash
# Build the database image
docker image build -t tools-db -f Dockerfile.db .

# Build the web image without embedded files
docker image build -t tools-web -f Dockerfile.web .

# Build the web image with embedded files
docker image build -t tools-web:embedded -f Dockerfile.web.embedded .

```

Containers can be run with the following commands:

```bash
# Run the database component
docker container run -d --name db --net app-net -e MYSQL_ROOT_PASSWORD=<some-pass> tools-db

# Run the web component without embedded (or with external) files
docker container run -d --name web --net app-net -p 8000:80 -v $(pwd)/web:/var/www/html tools-web

# Run the web component with embedded files
docker container run -d --name web --net app-net -p 8000:80 tools-web:embedded

```

Note that both containers should be attached to the same network to have working name resolution. The above sample commands expect the presense of the ***app-net*** network.

When built and deployed correctly, the result should look like this:

![preview of the working application](tools.png)

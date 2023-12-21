<font size=4 face='楷体'>

## 使用 Docker 镜像构建 Go 应用

### 环境准备

在进行 Docker 镜像构建之前，需要进行以下环境准备：

1. 安装[Docker](https://www.docker.com/get-started)
2. 安装[Go](https://golang.org/dl/)
3. [golang](https://hub.docker.com/_/golang) 官方镜像

### 创建 Go 应用

首先，需要创建一个简单的 Go 应用，例如一个 `Hello World` 程序。在本例中，创建一个名为 `main.go` 的文件，内容如下：

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello World!")
}
```

### 创建 Dockerfile

接下来，需要创建一个`Dockerfile`文件，用于构建 Docker 镜像。在本例中，创建一个名为`Dockerfile`的文件，内容如下：

```yaml
# 使用官方的 Golang 镜像作为构建环境
FROM golang:alpine AS builder

# 设置工作目录
WORKDIR /app

# 将代码加入镜像中
COPY . .

# 构建二进制文件
RUN GOOS=linux GOARCH=amd64 go build -o main main.go

# 使用最小化的 alpine 镜像作为运行环境
FROM alpine:latest

# 设置工作目录
WORKDIR /app

# 从之前构建的镜像中将二进制文件复制到 alpine 镜像中
COPY --from=builder /app/main .

# 运行二进制文件
CMD ["./main"]
```

以上 Dockerfile 包含了两个部分。第一部分以 golang:alpine 镜像为基础创建一个 builder，设置工作目录，将代码加入镜像中，然后构建二进制文件。第二部分以 alpine:latest 镜像为基础创建一个新的镜像，将之前构建的二进制文件从 builder 镜像中复制到新的镜像中，并设置工作目录和运行二进制文件。

### 构建 Docker 镜像

在 Dockerfile 和 Go 程序创建完成后，进入 Dockerfile 所在目录，执行以下命令来构建 Docker 镜像：

```bash
docker build -t my-go-application .
```

其中，`my-go-application`是镜像的名称，`.`表示 Dockerfile 所在的当前目录。

### 运行 Docker 镜像

构建 Docker 镜像完成后，可以使用以下命令来运行该镜像：

```bash
docker run -it --rm my-go-application
```

其中，`-it`参数表示以交互模式和终端模式运行容器，`--rm`参数表示容器停止后自动删除。

## 示例 1：使用 Docker Compose 构建多容器 Go 应用

在本示例中，将创建一个包含多个容器的 Docker Compose 项目，其中包括 Go 应用、MySQL 数据库和 phpMyAdmin 数据库管理工具。

### 创建一个新的 Go 应用

首先，创建一个名为`main.go`的文件，内容如下：

```go
package main

import (
    "database/sql"
    "fmt"
    "log"
    "net/http"
    "os"

    _ "github.com/go-sql-driver/mysql"
)

func main() {
    db, err := sql.Open("mysql", "root:password@tcp(db:3306)/testdb")
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    err = db.Ping()
    if err != nil {
        log.Fatal(err)
    }

    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Hello World!")
    })

    log.Fatal(http.ListenAndServe(":8080", nil))
}
```

以上 Go 应用连接到一个名为`testdb`的 MySQL 数据库，并在`/`路径下返回`Hello World!`字符串。

### 创建 Docker Compose 文件

接下来，创建一个名为`docker-compose.yml`的文件，内容如下：

```yaml
version: '3.9'

services:
  app:
    build: .
    ports:
      - '8080:8080'
    depends_on:
      - db

  db:
    image: mysql
    command: --default-authentication-plugin=mysql_native_password
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: testdb

  phpmyadmin:
    image: phpmyadmin/phpmyadmin
    depends_on:
      - db
    environment:
      PMA_HOST: db
      MYSQL_ROOT_PASSWORD: password
    ports:
      - '8081:80'
```

以上 Docker Compose 文件定义了三个服务：

1.  `app`服务：使用 Dockerfile 构建 Go 应用，并将容器内的 8080 端口映射到主机的 8080 端口。
2.  `db`服务：使用 MySQL 官方镜像创建一个 MySQL 数据库容器，并设置数据库的 root 密码为`password`，创建一个名为`testdb`的数据库。
3.  `phpmyadmin`服务：使用 phpMyAdmin 官方镜像创建一个 PHPMyAdmin 容器，连接到`db`服务之上，并将容器内的 80 端口映射到主机的 8081 端口。

### 运行 Docker Compose

在 Docker Compose 文件所在目录下，使用以下命令来启动所有的容器：

```bash
docker-compose up
```

运行完上述命令后，访问`http://localhost:8080`和`http://localhost:8081`可以分别查看 Go 应用和 phpMyAdmin 数据库管理工具。

### 停止 Docker Compose

使用以下命令来停止 Docker Compose：

```bash
docker-compose down
```

## 示例 2：使用 Docker Swarm 构建 Go 应用

在本示例中，将创建一个包含多个服务的 Docker Swarm 集群，其中包括 Go 应用和 MongoDB 数据库。

### 创建一个新的 Go 应用

首先，创建一个名为`main.go`的文件，内容如下：

```go
package main

import (
    "context"
    "fmt"
    "log"
    "net/http"
    "os"
    "time"

    "go.mongodb.org/mongo-driver/mongo"
    "go.mongodb.org/mongo-driver/mongo/options"
)

func main() {
    client, err := mongo.NewClient(options.Client().ApplyURI("mongodb://mongo:27017"))
    if err != nil {
        log.Fatal(err)
    }

    ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
    defer cancel()
    err = client.Connect(ctx)
    if err != nil {
        log.Fatal(err)
    }

    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        collection := client.Database("testdb").Collection("test")
        result, err := collection.InsertOne(context.Background(), map[string]string{"name": "John"})
        if err != nil {
            log.Fatal(err)
        }
        fmt.Fprintf(w, "Inserted document with ID %v\n", result.InsertedID)
    })

    log.Fatal(http.ListenAndServe(":8080", nil))
}
```

以上 Go 应用连接到一个名为`testdb`的 MongoDB 数据库，并在`/`路径下向`test`集合插入一个名为`John`的文档。

### 7.2 创建 Docker Compose 文件

接下来，创建一个名为`docker-compose.yml`的文件，内容如下：

```yaml
version: '3.9'

services:
  app:
    image: go-app
    deploy:
      replicas: 4
    ports:
      - '8080:8080'
    environment:
      MONGODB_URI: mongodb://mongo:27017
    networks:
      - webnet

  mongo:
    image: mongo
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: password
    networks:
      - webnet

networks:
  webnet:
```

以上 Docker Compose 文件定义了两个服务：

1.  `app`服务：使用 Docker 镜像构建 Go 应用，并在 Docker Swarm 集群中启动 4 个实例，将容器内的 8080 端口映射到主机的 8080 端口，并将 MongoDB 的 URI 设置为环境变量。
2.  `mongo`服务：使用 MongoDB 官方镜像创建一个 MongoDB 数据库容器，并设置数据库的 root 用户名和密码。

### 创建 Docker Swarm 集群

在执行以下命令之前，需要确保已经初始化 Docker Swarm 集群：

```bash
docker swarm init
```

### 构建和发布 Docker 镜像

首先，使用以下命令将 Go 应用构建成 Docker 镜像，并将其上传至 Docker Hub：

```bash
docker build -t my-go-app .
docker tag my-go-app:latest my-dockerhub-account/my-go-app:latest
docker push my-dockerhub-account/my-go-app:latest
```

其中，`my-dockerhub-account`为 Docker Hub 账户名。

### 部署 Docker 服务

接着，使用以下命令创建一个名为`webnet`的覆盖网络，并启动`app`和`mongo`服务：

```bash
docker network create --driver overlay webnet
docker stack deploy -c docker-compose.yml my-application
```

其中，`my-application`为服务的名称。

### 检查服务状态

使用以下命令检查已经启动的服务状态：

```bash
docker stack ps my-application
```

如果一切正常，则应该可以看到在 Docker Swarm 集群中启动了 4 个 Go 服务实例。当访问`http://localhost:8080`时，可以看到 Go 应用向 MongoDB 数据库中插入一个文档。

### 清除服务

使用以下命令清除所有服务：

```bash
docker stack rm my-application
docker network rm webnet
```

## 总结

本文分别介绍了使用 Docker 镜像构建 Go 应用的基本步骤、使用 Docker Compose 构建多容器 Go 应用的示例，以及使用 Docker Swarm 构建 Go 应用的示例。使用 Docker 镜像构建 Go 应用可以使得应用打包、部署和迁移更加方便、快速和高效。

### 报错

[What package should I install instead of libpcre++-dev to use C code in Alpine Golang?](https://stackoverflow.com/questions/58038858)
golang 官方 docker 镜像默认使用的是 Alpine, 尝试了很多方法也无法支持 golang 中的 pcre 或 pcre2 包的编译
大概是缺少 [pcre++.h](http://doc.gnu-darwin.org/libpcre++-0.6/pcre++_8h-source.html) 之类的头文件

### Reference

[使用 Docker 镜像构建 Go 应用的实现方法](https://pythonjishu.com/radsnqsvrkagqar/)

**2023.10.07**

<font size=4 face='楷体'>

## Dockerfile 简单示例

Dockerfile 是一个用来构建镜像的文本文件，文本内容包含了一条条构建镜像所需的指令和说明

- CentOS + Python3 + Pyinstaller
  构建 pyinstaller 打包环境

  ```dockerfile
    FROM centos:6
    SHELL ["/bin/bash", "-i", "-c"]

    # Target python version to build
    ARG PYTHON_VERSION=3.6.8
    # Target pyinstaller version
    ARG PYINSTALLER_VERSION=3.4

    # PYPI repository location
    ENV PYPI_URL=https://mirrors.aliyun.com/pypi
    # PYPI index location
    ENV PYPI_INDEX_URL=https://mirrors.aliyun.com/pypi/simple

    COPY entrypoint.sh /entrypoint.sh

    RUN \
        set -x \
        # update system
        && yum install -y yum && yum update -y \
        && yum install -y \
        git \
        readline-devel \
        zlib-devel \
        gcc \
        sqlite-devel \
        bzip2-devel \
        openssl \
        openssl-devel \
        make \
        patch \
        gcc-c++ \
        readline-devel \
        # install pyenv
        && echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc \
        && echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc \
        && source ~/.bashrc \
        && curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash \
        && echo 'eval "$(pyenv init -)"' >> ~/.bashrc \
        && source ~/.bashrc \
        # install python
        && PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install $PYTHON_VERSION \
        && pyenv global $PYTHON_VERSION \
        && pip install --upgrade pip \
        # install pyinstaller
        && pip install pyinstaller==$PYINSTALLER_VERSION \
        && mkdir /src/ \
        && chmod +x /entrypoint.sh

    VOLUME /src/
    WORKDIR /src/

    ENTRYPOINT ["/entrypoint.sh"]
  ```

  其中下载 pyenv 过程可能会受到 DNS 污染干扰 不稳定

  附脚本 `entrypoint.sh`

  ```bash
  #!/bin/bash -i

  # Fail on errors.
  set -e

  #
  # In case the user specified a custom URL for PYPI, then use
  # that one, instead of the default one.
  #
  if [[ "$PYPI_URL" != "https://pypi.python.org/" ]] || \
  [[ "$PYPI_INDEX_URL" != "https://pypi.python.org/simple" ]]; then
      # the funky looking regexp just extracts the hostname, excluding port
      # to be used as a trusted-host.
      mkdir -p /root/pip
      echo "[global]" > /root/pip/pip.conf
      echo "index = $PYPI_URL" >> /root/pip/pip.conf
      echo "index-url = $PYPI_INDEX_URL" >> /root/pip/pip.conf
      echo "trusted-host = $(echo $PYPI_URL | perl -pe 's|^.*?://(.*?)(:.*?)?/.*$|$1|')" >> /root/pip/pip.conf

      echo "Using custom pip.conf: "
      cat /root/pip/pip.conf
  fi

  cd /src

  if [ -f requirements.txt ]; then
      pip install -r requirements.txt
  fi # [ -f requirements.txt ]

  echo "$@"

  if [[ "$@" == "" ]]; then
      pyinstaller --clean -y --dist ./dist/linux --workpath /tmp *.spec
      chown -R --reference=. ./dist/linux
  else
      sh -c "$@"
  fi # [[ "$@" == "" ]]
  ```

  Dockerfile 与脚本文件准备好后执行

  ```bash
  sudo docker build -t pyinstaller:test .
  ```

  执行成功可见

  ```bash
  Successfully built IMAGE ID
  Successfully tagged pyinstaller:test
  ```

### Reference

[Lower GLIBC version](https://github.com/cdrx/docker-pyinstaller/issues/44)
[s0undt3ch/docker-pyinstaller](https://github.com/s0undt3ch/docker-pyinstaller/blob/e733792b89ddfb24e23e414ff2765255c08c99af/linux/py3/Dockerfile)
[pyenv-installer](https://github.com/pyenv/pyenv-installer)

**2020.6.9**

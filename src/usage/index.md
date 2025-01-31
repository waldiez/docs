
A jupyter lab extension is provided to help you get started with Waldiez. You can generate, convert and run Waldiez flows. Alternatively, you can use the Visual Studio Code extension: [Waldiez for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=Waldiez.waldiez-vscode).

!!! note
    Requirements:

    - Python >= 3.10, < 3.13

    For the Jupyter lab extension:

    - jupyterlab>=4.0.0,<5

### Manually

If not already, install jupyter:

```shell
pip install jupyter
```

Install the waldiez extension:

```shell
pip install waldiez-jupyter
```

Start jupyter lab:

```shell
jupyter lab
```

### Using Docker or Podman

Don't want to install anything? A docker image is also available, with jupyter and the waldiez extension pre-installed.

Pull the image:

```shell
docker pull waldiez/jupyter
```

Run the container:

```shell
# To share files with the container, 
# mount (for example) the `notebooks` directory:  
docker run -it -p 8888:8888 -v ${PWD}/notebooks:/home/user/notebooks waldiez/jupyter
```

Modify if needed, for example to use a different port:

```shell
docker run -p 10000:8888 -v ${PWD}/notebooks:/home/user/notebooks waldiez/jupyter
```

!!! note
    With podman and/or selinux, you might get permission errors, so you can try:
        ```shell
        podman run \
            --rm \
            -it \
            -p 10000:8888 \
            -v ${PWD}/notebooks:/home/user/notebooks \
            --userns=keep-id \
            --security-opt label=disable \
            waldiez/jupyter
        ```

You can now open your browser at `http://localhost:8888` (or the port you chose) and start [using Waldiez](models.md).

![Preview](../static/images/light//setup.webp#only-light)
![Dark Preview](../static/images/dark/setup.webp#only-dark)

[![Docker Pulls](https://img.shields.io/docker/pulls/waldiez/jupyter?cacheSeconds=3600)](https://hub.docker.com/r/waldiez/jupyter)
[![Docker Image Size (tag)](https://img.shields.io/docker/image-size/waldiez/jupyter/latest?cacheSeconds=3600)](https://hub.docker.com/r/waldiez/jupyter)

<!-- Available images:

- [Docker Hub](https://hub.docker.com/r/waldiez/jupyter)
  
- [Quay.io](https://quay.io/repository/waldiez/jupyter)
  
- [GitHub Container Registry](https://ghcr.io/waldiez/jupyter) -->

<!-- That's it! You can now open your browser at `http://localhost:8888` and start [using Waldiez](./usage.md). -->

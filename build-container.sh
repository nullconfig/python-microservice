#!/bin/bash

# Execute this script from the root directory of the repository to build the container
/usr/bin/docker build -t github-app -f $(pwd)/containerd/github-app.containerd $(pwd)
/usr/bin/docker build -t github-api -f $(pwd)/containerd/github-api.containerd $(pwd)

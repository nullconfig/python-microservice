#!/bin/bash

# Execute this script from the root directory of the repository to build the container
/usr/bin/docker build -t github-bot -f $(pwd)/containerd/python-app.containerd $(pwd)
/usr/bin/docker build -t github-api -f $(pwd)/containerd/python-api.containerd $(pwd)

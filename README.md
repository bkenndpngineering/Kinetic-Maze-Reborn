# Kinetic-Maze-Reborn
Kinetic Maze project implementation using Kinect-Skeleton-Tracker module

For documentation, see the project wiki.

## Python Dependencies
```
pip3 install pygame opencv-contrib-python openni
```

## Setup
1. See readmes of submodules for their dependencies and installation instructions. NiTE2 must be installed, instructions found in the Kinect Skeleton Tracker repo readme.
2. After downloading this repository, __before__ running the program.
  - Run the following:
    ```
    git submodules init
    git submodules update
    ```
  -**This step only needs to be done once post-install, or when submodules are updated**


## Running the program
To run the program, run `python3 main.py`.

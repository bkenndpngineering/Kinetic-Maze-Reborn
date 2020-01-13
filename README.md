# Kinetic-Maze-Reborn
Kinetic Maze project implementation using Kinect-Skeleton-Tracker module

For documentation, see the project wiki. If that's not complete (highly likely), see NotesForDevs.md.

## Python Dependencies
```
pip3 install pygame opencv-contrib-python openni
```

## Setup
1. See readmes of submodules for their dependencies and installation instructions. NiTE2 must be installed, instructions found in the Kinect Skeleton Tracker repo readme. Install instructions from Kinect_Skeleton_Tracker are copied below.
2. After downloading this repository, __before__ running the program.
  - Run the following:
    ```
    git submodules init
    git submodules update
    ```
  -**This step only needs to be done once post-install, or when submodules are updated** (may not work to update submodules)


### Dependencies for Kinect_Skeleton_Tracker
[Libfreenect](https://github.com/OpenKinect/libfreenect),
[Openni2](https://github.com/occipital/openni2),
[NiTE2](https://github.com/dpengineering/NiTE2/archive/v1.0.0.tar.gz)

#### Installing Dependencies
`sudo apt install freenect libopenni2-0 libopenni2-dev opencv-python`

##### Install NiTE:
1. Get NiTE:
  ```
  wget http://jaist.dl.sourceforge.net/project/roboticslab/External/nite/NiTE-Linux-x64-2.2.tar.bz2
  ```
2. Unpack NiTe:
  ```
  tar -xvjf NiTE-Linux-x64-2.2.tar.bz2
  ```
3. Copy binaries to the right directory:
  ```
  sudo ln -s $PWD/NiTE-Linux-x64-2.2/Redist/libNiTE2.so /usr/local/lib/
  sudo ln -s $PWD/NiTE-Linux-x64-2.2/Include /usr/local/include/NiTE-Linux-x64-2.2
  sudo ldconfig
  mkdir /usr/include/nite
  cp $PWD/NiTE-Linux-x64-2.2/Include/* /usr/include/nite/
  cp $PWD/NiTE-Linux-x64-2.2/Redist/libNiTE2.so /usr/lib/
  cp -r $PWD/NiTE-Linux-x64-2.2/Redist/NiTE2 /usr/lib/
  ```
4. Fix headers
  - Change Niteheaders to use correct openni headers <openni2/package> instead of old <package> anything with OniXXXXXXX
  ```
  sudo vim /usr/include/nite/NiteCAPI.h
  sudo vim /usr/include/nite/NiteCTypes.h
  sudo vim /usr/include/nite/NiteVersion.h
  sudo vim /usr/include/nite/NiTE.h
  ```

5. Build OpenNNI2-FreenectDriver
  ```
  sudo apt install cmake make build-essential git
  sudo apt install libusb-dev
  git clone https://github.com/OpenKinect/libfreenect
  cd libfreenect
  mkdir build
  cd build
  cmake .. -DBUILD_OPENNI_DRIVER=ON
  cd .. # sometimes the makefile is in a different directory. use your eyes
  make
  ```
6. place libFreenectDriver.so.0 in /usr/lib/OpenNI2/Drivers
  ```
  cp libFreenectDriver.so /usr/lib/OpenNI2/Drivers/
  cp libFreenectDriver.so libFreenectDriver.so.0 			# need to be a .so.0 for some reason
  ```

 NiTE2 must be kept in the same directory as tracker! Copy the NiTE-Linux-x64-2.2/Redist/NiTE2 directory and its contents into the project directory (same place as script).



## Running the program
To run the program, run `python3 main.py`.

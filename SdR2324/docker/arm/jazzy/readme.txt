Running ROS 2 nodes in Docker [community-contributed]
https://docs.ros.org/en/jazzy/How-To-Guides/Run-2-nodes-in-single-or-separate-docker-containers.html

Experimenting with a dummy robot
https://docs.ros.org/en/jazzy/Tutorials/Demos/dummy-robot-demo.html


echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
source ~/.bashrc

YouTube video:
https://www.youtube.com/watch?v=ECaBsKY9rUM

Per completare l'installazione:

wget https://s3.ap-northeast-1.wasabisys.com/download-raw/dpkg/ros2-desktop/debian/bookworm/ros-jazzy-desktop-0.3.2_20240525_arm64.deb
apt install ./ros-jazzy-desktop-0.3.2_20240525_arm64.deb 
apt install net-tools

# When using Rviz2, switch the display server from Wayland to X11
apt get install xorg openbox
# poi lanciare raspi-config
#   selezionare "Advanced Options"
#     poi selezionare Wayland
#       infine selezione X11
# poi: reboot

apt install mc arj genisoimage imagemagick unar wimtools
apt install shotwell


costruzione del pacchetto:
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
# This repository contains source code for demos mentioned in the official ROS 2 documentation
git clone -b jazzy https://github.com/ros2/demos
source /opt/ros/jazzy/setup.bash
colcon build --packages-up-to dummy_robot_bringup
source ~/ros2_ws/install/setup.bash


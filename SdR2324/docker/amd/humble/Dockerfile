# This is an Dockerfile for ros:humble-desktop-full
FROM ghcr.io/sloretz/ros:humble-desktop-full

# update e upgrade
RUN apt update && \
    apt upgrade -y
# install ros-gz
#RUN apt install -y \
#ros-humble-ros-gz \
#ros-humble-ros-gz-bridge \
#ros-humble-ros-gz-bridge-dbgsym \
#ros-humble-ros-gz-image \
#ros-humble-ros-gz-image-dbgsym \
#ros-humble-ros-gz-interfaces \
#ros-humble-ros-gz-interfaces-dbgsym \
#ros-humble-ros-gz-sim \
#ros-humble-ros-gz-sim-dbgsym \
#ros-humble-ros-gz-sim-demos
# install turtlebot3 examples

wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
   30  echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" |  tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
apt-get update
apt-get install ignition-fortress


RUN apt install -y  ros-humble-turtlebot3 && \
    apt install -y  ros-humble-turtlebot3-gazebo && \
    apt install -y  ros-humble-turtlebot3-simulations && \
    apt clean
RUN apt install -y software-properties-common ros-dev-tools
# install editors
RUN apt install -y nano vim exuberant-ctags vim-scripts tmux vim-addon-manager vim-editorconfig vim-pathogen mc arj  lynx unar zip

#apt install -y  ros-humble-slam-gmapping && \ abbandonato in ROS2

## Download and build our Robot and Simulation application
#RUN sh -c 'mkdir -p /root/SdR/workspace'
#RUN sh -c 'cd /root/SdR/workspace && wget https://github.com/sdoro/phycomp/archive/refs/heads/main.zip && unzip main.zip'

COPY ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]

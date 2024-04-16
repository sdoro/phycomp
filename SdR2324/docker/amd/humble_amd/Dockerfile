# This is an Dockerfile for ros:humble-ros-base-jammy
FROM ros:humble-ros-base-jammy

# install humble packages

# update e upgrade
RUN apt update && \
    apt upgrade -y

# install missing (for arm) gazebo package
#RUN apt-get install software-properties-common -y && \
#    add-apt-repository ppa:openrobotics/gazebo11-non-amd64 && \
#    apt update && \
#    apt-get install gazebo -y

# customize image ...
RUN apt-get install -y --no-install-recommends ros-humble-desktop-full && \
    apt install -y --no-install-recommends ros-humble-gazebo-* && \
    apt install -y --no-install-recommends ros-humble-cartographer && \
    apt install -y --no-install-recommends ros-humble-cartographer-ros && \
    apt install -y --no-install-recommends ros-humble-navigation2 && \
    apt install -y --no-install-recommends ros-humble-nav2-bringup && \
    apt install -y --no-install-recommends ros-humble-dynamixel-sdk
#
RUN apt install -y --no-install-recommends ros-humble-turtlebot3-msgs && \
    apt install -y --no-install-recommends ros-humble-turtlebot3 && \
    apt install -y --no-install-recommends ros-humble-turtlebot3-* 
#
RUN apt install -y --no-install-recommends ros-humble-turtlebot4-simulator && \
    apt install -y --no-install-recommends ros-humble-turtlebot4-desktop && \
    apt install -y --no-install-recommends ros-humble-turtlebot4-tests && \
    apt install -y --no-install-recommends ros-humble-turtlebot4-python-tutorials && \
    apt install -y --no-install-recommends ros-humble-turtlebot4-tutorials && \
    apt clean

COPY ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]

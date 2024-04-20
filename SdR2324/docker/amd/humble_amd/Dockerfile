# This is an Dockerfile for ros:humble-ros-base-jammy
#FROM ros:humble-ros-base-jammy
FROM ghcr.io/sloretz/ros:humble-desktop-full

# update e upgrade
RUN apt update && \
    apt upgrade -y
# install turtlebot3 examples
RUN apt install -y  ros-humble-turtlebot3 && \
    apt install -y  ros-humble-turtlebot3-gazebo && \
    apt install -y  ros-humble-turtlebot3-simulations && \
    apt clean

#apt install -y  ros-humble-slam-gmapping && \

COPY ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]

#FROM ros:noetic-ros-base-focal
# https://community.gazebosim.org/t/up-to-date-docker-images-for-gazebo-ros-using-the-osrf-repo/2717
FROM ghcr.io/sloretz/ros:humble-desktop-full

RUN apt update && \
    apt upgrade -y
# install turtlebot3 examples
RUN apt install -y  ros-humble-turtlebot3 && \
    apt clean

#    apt install -y  ros-noetic-slam-gmapping && \
#    apt install -y  ros-humble-turtlebot3-gazebo && \
#    apt install -y  ros-humble-turtlebot3-simulations && \

COPY ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]


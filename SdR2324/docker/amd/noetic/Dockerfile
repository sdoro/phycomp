# This is an Dockerfile for ros:humble-ros-base-jammy
#FROM ros:humble-ros-base-jammy
FROM osrf/ros:noetic-desktop-full

# update e upgrade
RUN apt update

RUN apt-get install -y  ros-noetic-turtlebot3 && \
    apt install -y  ros-noetic-turtlebot3-gazebo && \
    apt install -y  ros-noetic-turtlebot3-simulations && \
    apt install -y  ros-noetic-slam-gmapping && \
    apt clean

#COPY ros_entrypoint.sh /

#ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]

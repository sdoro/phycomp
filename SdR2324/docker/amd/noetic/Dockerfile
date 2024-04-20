# 
FROM osrf/ros:noetic-desktop-full

# update e upgrade
RUN apt update && \
    apt upgrade -y
# install turtlebot3 examples
RUN apt install -y  ros-noetic-turtlebot3 && \
    apt install -y  ros-noetic-turtlebot3-gazebo && \
    apt install -y  ros-noetic-turtlebot3-simulations && \
    apt install -y  ros-noetic-slam-gmapping && \
    apt clean

COPY ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]


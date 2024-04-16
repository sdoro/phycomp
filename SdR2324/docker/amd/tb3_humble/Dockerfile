FROM osrf/ros:humble-desktop

WORKDIR /app

# update & upgrade
RUN apt update --allow-insecure-repositories && \ 
    apt upgrade -y 
# Install ROS 2 packages
RUN apt install -y ros-humble-gazebo-* && \
    apt install -y ros-humble-cartographer && \
    apt install -y ros-humble-cartographer-ros && \
    apt install -y ros-humble-navigation2 && \
    apt install -y ros-humble-nav2-bringup && \
    apt install -y ros-humble-dynamixel-sdk
# Install TurtleBot3
RUN apt install -y ros-humble-turtlebot3 && \
    apt install -y ros-humble-turtlebot3-*
# cleanup
RUN apt clean

COPY ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["bash"]

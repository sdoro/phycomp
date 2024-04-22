#FROM ros:noetic-ros-base-focal
# https://community.gazebosim.org/t/up-to-date-docker-images-for-gazebo-ros-using-the-osrf-repo/2717
FROM ghcr.io/sloretz/ros:humble-desktop-full

RUN apt update && \
    apt upgrade -y

# install missing (for arm) gazebo package
RUN apt-get install software-properties-common -y && \
    add-apt-repository ppa:openrobotics/gazebo11-non-amd64 && \
    apt update && \
    apt-get install gazebo -y

# install turtlebot3 examples
RUN apt install -y  ros-humble-gazebo-* && \
    apt install -y  ros-humble-turtlebot3 && \
    apt clean
# install missing editors
RUN apt install nano vim exuberant-ctags vim-scripts tmux vim-addon-manager vim-editorconfig vim-pathogen mc arj  lynx unar zip

#    apt install -y  ros-noetic-slam-gmapping && \
#    apt install -y  ros-humble-turtlebot3-gazebo && \
#    apt install -y  ros-humble-turtlebot3-simulations && \

COPY ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]


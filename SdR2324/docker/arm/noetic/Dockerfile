#FROM ros:noetic-ros-base-focal
# https://community.gazebosim.org/t/up-to-date-docker-images-for-gazebo-ros-using-the-osrf-repo/2717
FROM ghcr.io/sloretz/ros:noetic-simulators-osrf

RUN apt update && \
    apt upgrade -y
# install turtlebot3 examples
RUN apt install -y  ros-noetic-turtlebot3 && \
    apt install -y  ros-noetic-turtlebot3-gazebo && \
    apt install -y  ros-noetic-turtlebot3-simulations && \
    apt install -y  ros-noetic-slam-gmapping && \
    apt clean
# install missing editors
RUN apt install -y nano vim exuberant-ctags vim-scripts tmux vim-addon-manager vim-editorconfig vim-pathogen mc arj  lynx unar zip

COPY ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]


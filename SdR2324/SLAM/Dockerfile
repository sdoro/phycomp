FROM osrf/ros:noetic-desktop-full

RUN apt update

RUN apt install -y vim exuberant-ctags vim-doc vim-scripts
RUN apt install -y colordiff bleachbit cream tmux vim-addon-manager vim-editorconfig vim-pathogen vim-puppet vim-rails vim-tabular
RUN apt install -y mc arj catdvi dbview epub-utils imagemagick lynx unar
RUN apt install -y git gitg gitk
RUN apt clean

RUN apt install -y ros-noetic-universal-robots
RUN apt install -y ros-noetic-turtlebot3\*

RUN echo "export TURTLEBOT3_MODEL=burger" >> .bashrc

RUN echo "ALL DONE !"


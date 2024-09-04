#FROM ros:noetic-ros-base-focal
# https://community.gazebosim.org/t/up-to-date-docker-images-for-gazebo-ros-using-the-osrf-repo/2717
FROM ghcr.io/sloretz/ros:jazzy-desktop-full

RUN apt update && \
    apt upgrade -y

COPY ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]


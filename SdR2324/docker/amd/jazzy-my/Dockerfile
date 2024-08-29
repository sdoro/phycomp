
#
FROM ghcr.io/sloretz/ros:jazzy-desktop-full

# update e upgrade
RUN apt update && \
    apt upgrade -y

RUN apt install -y vim mc less && \
    apt install -y ros-jazzy-ros-gz ros-jazzy-ros-gz-sim && \
    apt install -y ros-jazzy-robot-localization && \
    apt install -y ros-jazzy-controller-manager && \
    apt install -y ros-jazzy-ros2-control && \
    apt install -y ros-jazzy-ros2-controllers && \
    apt install -y ros-jazzy-gz-ros2-control && \
    apt install -y ros-jazzy-gz-ros2-control-demos && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*


COPY ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["bash"]

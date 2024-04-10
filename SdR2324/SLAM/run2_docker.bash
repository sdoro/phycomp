
xhost local:root

XAUTH=/tmp/.docker.xauth

docker run -it \
	--name=linux_gui_r1 \
	--env="DISPLAY=$DISPLAY" \
	--env="QT_X11_NO_MITSHM=1" \
	--volume="/tmp/.X11-unix:/tmp/-X11-unix:rw" \
	--env="XAUTHORITY=$XAUTH" \
	--volume="$XAUTH:$XAUTH" \
	--net=host \
	--privileged \
	osrf/ros:noetic-desktop-full \
	roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch

echo "Done."


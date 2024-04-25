
xhost local:root

XAUTH=/tmp/.docker.xauth

docker exec -it \
	--env="DISPLAY=$DISPLAY" \
	--env="QT_X11_NO_MITSHM=1" \
	--env="XAUTHORITY=$XAUTH" \
	--env="ROS_DOMAIN_ID=5" \
	--privileged \
	SdR \
	bash

echo "Done."


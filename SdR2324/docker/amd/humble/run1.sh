
xhost local:root

XAUTH=/tmp/.docker.xauth

docker run -it \
	--name=SdR \
	--rm \
	--env="DISPLAY=$DISPLAY" \
	--env="QT_X11_NO_MITSHM=1" \
	--env="ROS_DOMAIN_ID=5" \
	--volume="/tmp/.X11-unix:/tmp/-X11-unix:rw" \
	--env="XAUTHORITY=$XAUTH" \
	--volume="$XAUTH:$XAUTH" \
	--net=host \
	--privileged \
	--volume .:/mnt/share \
	sdoro/humble_sdr_amd:latest \
	bash

echo "Done."


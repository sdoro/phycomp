
xhost local:root

XAUTH=/tmp/.docker.xauth

docker run -it \
	--name=t3h \
	--rm \
	--env="DISPLAY=$DISPLAY" \
	--env="QT_X11_NO_MITSHM=1" \
	--volume="/tmp/.X11-unix:/tmp/-X11-unix:rw" \
	--env="XAUTHORITY=$XAUTH" \
	--volume="$XAUTH:$XAUTH" \
	--net=host \
	--privileged \
	sdoro/humble_sdr_amd \
	bash

echo "Done."


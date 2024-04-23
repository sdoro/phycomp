

XAUTH=/tmp/.docker.xauth

docker exec -it \
	--env="DISPLAY=$DISPLAY" \
	--env="QT_X11_NO_MITSHM=1" \
	--env="XAUTHORITY=$XAUTH" \
	--privileged \
	linux_gui_r1 \
	bash

echo "Done."


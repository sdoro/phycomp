Running ROS 2 nodes in Docker [community-contributed]
https://docs.ros.org/en/jazzy/How-To-Guides/Run-2-nodes-in-single-or-separate-docker-containers.html

Experimenting with a dummy robot
https://docs.ros.org/en/jazzy/Tutorials/Demos/dummy-robot-demo.html


echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
source ~/.bashrc

apt install ros-${ROS_DISTRO}-dummy-robot-bringup
ros2 launch dummy_robot_bringup dummy_robot_bringup_launch.py

Una eventuale configurazione finale di rviz2 si trova nel file config.rviz


YouTube video:
https://www.youtube.com/watch?v=ECaBsKY9rUM


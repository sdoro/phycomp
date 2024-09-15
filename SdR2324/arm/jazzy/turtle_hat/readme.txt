

source /opt/ros/jazzy/setup.bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src


# Create a Package (note dependencies!)
ros2 pkg create --build-type ament_python build_hat --dependencies rclpy geometry_msgs

cd ~/ros2_ws
cp prova_sub.py ~/ros2_ws/src/build_hat/build_hat/prova_sub.py
# compile only my_package
colcon build --packages-select build_hat


# Create a Launch File
cd ~/ros2_ws/src/build_hat
mkdir launch
cd ~/ros2_ws/src/build_hat/launch
touch build_hat_launch_file.launch.py
chmod +x build_hat_launch_file.launch.py
cd ~/ros2_ws
# copy files:
cp build_hat_launch_file.launch.py src/build_hat/launch/build_hat_launch_file.launch.py
cp setup.py src/build_hat/setup.py

cd ~/ros2_ws
# compile only my_package
colcon build --packages-select build_hat

# run!
source ~/ros2_ws/install/setup.bash
#ros2 launch build_hat build_hat_launch_file.launch.py
ros2 run build_hat prova_subscribe


# genero/publico un Twist:
ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"

# bot

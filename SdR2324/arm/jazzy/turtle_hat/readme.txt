

source /opt/ros/jazzy/setup.bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src


# Create a Package
ros2 pkg create --build-type ament_python build_hat --dependencies rclpy geometry_msgs

cd ~/ros2_ws
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
source install/setup.bash
ros2 launch build_hat build_hat_launch_file.launch.py

# bot

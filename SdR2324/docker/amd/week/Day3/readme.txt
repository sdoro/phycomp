
./install.sh
./course_install.sh

source ~/sim_ws/install/setup.bash
ros2 launch rosbot_xl_gazebo simulation.launch.py

./first.sh
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap cmd_vel:=/rosbot_xl_base_controller/cmd_vel


# Create a Package

source /mnt/share/first.sh
cd ~

source /opt/ros/jazzy/setup.bash
cd ~/ros2_ws/
cd src
ros2 pkg create --build-type ament_python my_package --dependencies rclpy
cd ..
# compile only my_package
colcon build --packages-select my_package
source install/setup.bash
ros2 pkg list | grep my_package


# What is a Launch File? 

cd ~/ros2_ws/src/my_package
mkdir launch
cd ~/ros2_ws/src/my_package/launch
touch my_package_launch_file.launch.py
chmod +x my_package_launch_file.launch.py
cd ~/ros2_ws

cp /mnt/share/my_package_launch_file.launch.py src/my_package/launch/my_package_launch_file.launch.py
cp /mnt/share/setup.py src/my_package/setup.py

colcon build --packages-select my_package
source install/setup.bash
ros2 launch my_package my_package_launch_file.launch.py


--- per i demo ---

Invece funzionano i some examples in the ign_ros2_control_demos package
installati con il comando:

apt install ros-jazzy-gz-ros2-control-demos

per farli partire si segue:

https://github.com/ros-controls/gz_ros2_control/blob/c21f472743dfd1993c5e8d5952f1109ba248d0df/doc/index.rst#ign_ros2_control_demos

ma attenzione a cambiare, ad esempio, ign_ros2_control_demos in gz_ros2_control_demos in tutte le stringhe.


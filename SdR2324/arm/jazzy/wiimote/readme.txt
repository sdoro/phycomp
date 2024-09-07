
source /opt/ros/jazzy/setup.bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/ros-drivers/joystick_drivers.git -b ros2
colcon build --packages-up-to wiimote
source install/setup.bash

ros2 launch wiimote turtlesim.launch.py



source /opt/ros/jazzy/setup.bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/ros-drivers/joystick_drivers.git -b ros2
colcon build --packages-up-to wiimote
source install/setup.bash

ros2 launch wiimote turtlesim.launch.py

-------

// Sane defaults based on the TurtleBot3
// max linear speed = 0.22 m/s
// maxi angular speed = 2.84 rad/s


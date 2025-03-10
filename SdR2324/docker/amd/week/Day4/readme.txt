
# redefine HOME
source /mnt/share/first.sh

# install mine packages
/mnt/share/install.sh

# install packages for day 4
/mnt/share/course_install.sh

# copy project
tar zxf /mnt/share/ros2-learning-week-day-4-under--2024-08-03--e98949628832.tgz


source ~/sim_ws/install/setup.bash
# ? source ./sim_ws/install/local_setup.bash
ros2 launch rosbot_xl_gazebo simulation.launch.py


source /opt/ros/jazzy/setup.bash
# try to get some information about /rosbot_xl_base_controller/cmd_vel
ros2 topic info /rosbot_xl_base_controller/cmd_vel
# try to get some information about /scan
ros2 topic info /scan
# try to get some information about /camera/color/image_raw
ros2 topic info /camera/color/image_raw
# to get information about a specific interface (geometry_msgs/msg/TwistStamped)
ros2 interface show geometry_msgs/msg/TwistStamped
# publishing information in the /rosbot_xl_base_controller/cmd_vel topic.
# To do this, send a message to the geometry_msgs/msg/TwistStamped interface
ros2 topic pub /rosbot_xl_base_controller/cmd_vel geometry_msgs/msg/TwistStamped
"header:
  stamp:
    sec: 0
    nanosec: 0
  frame_id: ''
twist:
  linear:
    x: 0.0
    y: 0.0
    z: 0.0
  angular:
    x: 0.0
    y: 0.0
    z: 0.5
"

ros2 topic info /scan
# find important information /scan topic
ros2 interface show sensor_msgs/msg/LaserScan


# create a Simple Publisher Node
--------------------------------
cd ~/ros2_ws/src/
ros2 pkg create --build-type ament_python publisher_pkg --dependencies rclpy std_msgs geometry_msgs
cp /mnt/share/simple_publisher.py publisher_pkg/publisher_pkg/
cd ~/ros2_ws/src/publisher_pkg
mkdir launch
cd ~/ros2_ws/src/publisher_pkg/launch
touch publisher_pkg_launch_file.launch.py
chmod +x publisher_pkg_launch_file.launch.py
cp /mnt/share/publisher_pkg_launch_file.launch.py .
cd ~/ros2_ws/src/publisher_pkg
cp  /mnt/share/setupPub.py setup.py
cd ~/ros2_ws
colcon build --packages-select publisher_pkg
source ~/ros2_ws/install/setup.bash
ros2 launch publisher_pkg publisher_pkg_launch_file.launch.py


# create a Simple Subscriber Node
---------------------------------
cd ~/ros2_ws/src/
ros2 pkg create --build-type ament_python subscriber_pkg --dependencies rclpy std_msgs sensor_msgs
cp /mnt/share/simple_subscriber.py subscriber_pkg/subscriber_pkg/
cd ~/ros2_ws/src/subscriber_pkg
mkdir launch
cd ~/ros2_ws/src/subscriber_pkg/launch
touch subscriber_pkg_launch_file.launch.py
chmod +x subscriber_pkg_launch_file.launch.py
cp /mnt/share/subscriber_pkg_launch_file.launch.py .
cd ..
cp /mnt/share/setupSub.py setup.py
cd ~/ros2_ws
colcon build --packages-select subscriber_pkg
source ~/ros2_ws/install/setup.bash
ros2 launch subscriber_pkg subscriber_pkg_launch_file.launch.py
# in another terminal:
ros2 topic info /scan -v


# Write a Publisher & Subscriber Node
-------------------------------------
cd ~/ros2_ws/src/
ros2 pkg create --build-type ament_python exercise21_pkg --dependencies rclpy std_msgs sensor_msgs geometry_msgs
cp /mnt/share/exercise21.py exercise21_pkg/exercise21_pkg/
cd ~/ros2_ws/src/exercise21_pkg
mkdir launch
cd ~/ros2_ws/src/exercise21_pkg/launch/
touch exercise21_pkg_launch_file.launch.py
chmod +x exercise21_pkg_launch_file.launch.py
cp /mnt/share/exercise21_pkg_launch_file.launch.py .
cd ..
cp /mnt/share/setupPubSub.py setup.py
colcon build --packages-select exercise21_pkg
source ~/ros2_ws/install/setup.bash
ros2 launch exercise21_pkg exercise21_pkg_launch_file.launch.py


# How to Create a Custom Interface
----------------------------------
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_cmake custom_interfaces
cd ~/ros2_ws/src/custom_interfaces
mkdir msg
cp /mnt/share/Age.msg msg/
cp /mnt/share/CMakeLists.txt .
cp /mnt/share/package.xml .
cd ~/ros2_ws
colcon build --packages-select custom_interfaces
source install/setup.bash

# verify the message has been created:
ros2 interface show custom_interfaces/msg/Age


# Use a Custom Interface
------------------------
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python example26_pkg --dependencies rclpy std_msgs geometry_msgs custom_interfaces
cd ~/ros2_ws/src/example26_pkg
cp /mnt/share/example26.py example26_pkg/
mkdir launch
cd launch
touch example26.launch.py
chmod +x example26.launch.py
cp /mnt/share/example26.launch.py example26.launch.py
cd ..
cp /mnt/share/setupCusInt.py setup.py
cd ~/ros2_ws
colcon build --packages-select example26_pkg
source ~/ros2_ws/install/setup.bash
ros2 launch example26_pkg example26.launch.py
# in other term
source /mnt/share/first.sh
source ~/ros2_ws/install/setup.bash
ros2 topic echo /age


# bot

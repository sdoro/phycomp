
# redefine HOME
source /mnt/share/first.sh

# install packages for day 4
/mnt/share/course_install.sh

# copy project
tar zxf /mnt/share/ros2-learning-week-day-4-under--2024-08-03--e98949628832.tgz


source ~/sim_ws/install/setup.bash
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
# find important information /scan topic
ros2 interface show sensor_msgs/msg/LaserScan


# create a Simple Publisher Node
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

# create a Simple Subscriber Node
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


# bot

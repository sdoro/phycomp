from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='example26_pkg',
            executable='example26_node',
            output='screen'),
    ])

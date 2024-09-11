from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='build_hat',
            executable='prova_subscribe',
            output='screen'),
    ])


from buildhat import Hat
from buildhat import MotorPair

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            'turtle1/cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.hat = Hat()
        self.get_logger().info('Firmware loaded!')
        self.pair = MotorPair('A', 'B')

    def listener_callback(self, msg):
        self.get_logger().info('I heard a Twist: LinVel="%f", AngVel="%f"' % (msg.linear.x, msg.angular.z))
        lx = msg.linear.x
        az = msg.angular.z
        if lx > 0.1:
            self.pair.run_for_rotations(0.25, speedl=-5, speedr=5)
        elif lx < -0.1:
            self.pair.run_for_rotations(0.25, speedl=5, speedr=-5)

        if az > 0.1:
            self.pair.run_for_rotations(0.25, speedl=5, speedr=5)
        elif az < -0.1:
            self.pair.run_for_rotations(0.25, speedl=-5, speedr=-5)

        self.pair.stop()

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

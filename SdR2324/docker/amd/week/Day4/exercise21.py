import rclpy
# import the ROS2 python libraries
from rclpy.node import Node
# import the TwistStamped module from geometry_msgs interface
from geometry_msgs.msg import TwistStamped
# import the LaserScan module from sensor_msgs interface
from sensor_msgs.msg import LaserScan
from rclpy.qos import ReliabilityPolicy, QoSProfile

class Exercise21(Node):

    def __init__(self):
        # Here we have the class constructor
        # call the class constructor
        super().__init__('exercise21')
        # create the publisher object
        self.publisher_ = self.create_publisher(TwistStamped, '/rosbot_xl_base_controller/cmd_vel', 10)
        # create the subscriber object
        self.subscriber = self.create_subscription(LaserScan, '/scan', self.laser_callback, QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT))
        # prevent unused variable warning
        self.subscriber
        # define the timer period for 0.5 seconds
        self.timer_period = 0.5
        # define the variable to save the received info
        self.laser_forward = 0
        # create a TwistStamped message
        self.cmd = TwistStamped()
        self.timer = self.create_timer(self.timer_period, self.motion)

    def laser_callback(self,msg):
        # Save the frontal laser scan info at 0°
        self.laser_forward = msg.ranges[0]      

    def motion(self):
        # print the data
        self.get_logger().info('I receive: "%s"' % str(self.laser_forward))
        # Logic of move
        if self.laser_forward > 3:
            self.cmd.twist.linear.x = 0.5
            self.cmd.twist.angular.z = 0.0
        elif self.laser_forward < 3 and self.laser_forward >= 1:
            self.cmd.twist.linear.x = 0.3
            self.cmd.twist.angular.z = 0.0          
        else:
            self.cmd.twist.linear.x = 0.1
            self.cmd.twist.angular.z = -1.0
        # Publishing the cmd_vel values to topipc
        self.publisher_.publish(self.cmd)


            
def main(args=None):
    # initialize the ROS communication
    rclpy.init(args=args)
    # declare the node constructor
    exercise21 = Exercise21()       
    # pause the program execution, waits for a request to kill the node (ctrl+c)
    rclpy.spin(exercise21)
    # Explicity destroy the node
    exercise21.destroy_node()
    # shutdown the ROS communication
    rclpy.shutdown()

if __name__ == '__main__':
    main()

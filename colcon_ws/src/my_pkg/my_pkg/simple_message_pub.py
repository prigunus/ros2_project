import rclpy 
from rclpy.node import Node
from rclpy.qos import QoSProfile
from rclpy.qos import QoSHistoryPolicy, QoSReliabilityPolicy, QoSDurabilityPolicy
from std_msgs.msg import String
from rclpy.clock import ClockType, Clock
from geometry_msgs.msg import Twist
from std_msgs.msg import Header

class M_pub(Node):
    def __init__(self):
        super().__init__('simple_mpub')
        self.qos_profile = QoSProfile(depth=10)
        self.pub = self.create_publisher(String, 'message', self.qos_profile)
        self.timer = self.create_timer(1, self.spin_msg)

    def spin_msg(self):
        msg = String()
        msg.data = 'hellow'
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = M_pub()

    try:
        rclpy.spin(node) # block funtion
    except KeyboardInterrupt:
        node.get_logger().info("keyboard interrupt!!!")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

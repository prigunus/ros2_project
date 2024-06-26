import rclpy 
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String

def spin_msg():
    pub.publish(msg)

def main(args=None):

    node = Node('simple_msub')
    self.qos_profile = QoSProfile(depth=10)
    pub = node.create_subscription(String, 'message', self.sub_message, self.qos_profile)

    msg = String()
    msg.data = 'hello'
    timer = node.create_timer(1, spin_msg)
    rclpy.spin(node) # block funtion
    print('this is mpub code')

if __name__ == '__main__':
    main()
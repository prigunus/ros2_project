import rclpy
from rclpy.node import Node

class smp_cs(Node):
    def __init__(self):
        super().__init__('chang')
        

def main(args=None):
    print('hello ros2!!!')
    rclpy.init(args=args)
    node = smp_cs()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('keyboard interrupt!!')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
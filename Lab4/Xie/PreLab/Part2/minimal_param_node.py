import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor


class MinimalParamNode(Node):
    def __init__(self):
        super().__init__('minimal_param_node')

        # existing parameter
        self.declare_parameter(
            'my_parameter',
            'default',
            ParameterDescriptor(description='A string parameter to print')
        )
        self.my_param = self.get_parameter('my_parameter').get_parameter_value().string_value

        # PreLab 4 Part 2: add wait_time parameter (double_value)
        self.declare_parameter(
            'wait_time',
            1.0,
            ParameterDescriptor(description='Time between prints (sec)')
        )
        self.wait_time = self.get_parameter('wait_time').get_parameter_value().double_value

        self.get_logger().info(f"Started minimal_param_node with my_parameter='{self.my_param}', wait_time={self.wait_time}")
        self.timer = self.create_timer(self.wait_time, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info(f"my_parameter: {self.my_param}")


def main(args=None):
    rclpy.init(args=args)
    node = MinimalParamNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

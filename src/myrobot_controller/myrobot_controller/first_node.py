#!/usr/bin/env python3
from typing import List
import rclpy
from rclpy.context import Context
from rclpy.node import Node
from rclpy.parameter import Parameter


class MyNode(Node):
    def __init__(self):
        super().__init__("my_node") # creat the node name
        # timer will call function every 1 second
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        
        self.counter_ += 1
        self.get_logger().info(f"Hello {self.counter_}")


def main(args=None):
    # initialize ros2 communication
    rclpy.init(args=args)
    
    # content during communication session
    node = MyNode()

    
    rclpy.spin(node) # keep running node untill external interrupt
    rclpy.shutdown()

if __name__ == "__main__":
    main()
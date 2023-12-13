#!/usr/bin/env python3
# start with the turtlesim by:
# ros2 run turtlesim turtlesim_node
from typing import List
import rclpy
from rclpy.context import Context
from rclpy.node import Node
from rclpy.parameter import Parameter
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.cmd_vel_publisher = self.create_publisher(
            Twist, "/turtle1/cmd_vel", 10)
        # everything receive the subscription, execute the 
        # callback function
        self.pose_subscriber = self.create_subscription(
            Pose, "/turtle1/pose", self.pose_callback, 10)
        
        self.get_logger().info("turtle_controller started")

    def pose_callback(self, msg:Pose):
        cmd = Twist()
        if msg.x > 9.0 or msg.x < 2.0 or msg.y > 9.0 or msg.y < 2.0:
            cmd.linear.x = 1.0
            cmd.angular.z = 0.9
            self.cmd_vel_publisher.publish(cmd)
        else:
            cmd.linear.x = 5.0
            cmd.angular.z = 0.0
            self.cmd_vel_publisher.publish(cmd)
        
        


def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()
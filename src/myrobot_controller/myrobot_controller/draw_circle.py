#!/usr/bin/env python3
# A demo program to manipulate the turtlesimu
# to draw a circle by publish the velocity msg

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):
    def __init__(self):
        super().__init__("draw_circle")
        #create the publisher (topic message sender)
        
        self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.create_timer(1.0, self.send_velocity_cmd)

        self.get_logger().info("draw_circle node started")

    def send_velocity_cmd(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub.publish(msg)



def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()
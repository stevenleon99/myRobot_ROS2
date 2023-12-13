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
from turtlesim.srv import SetPen
from functools import partial

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
        
        if msg.x > 5.5:
            self.get_logger().info("set color to red")
            self.call_setpen_service(255, 0, 0, 3, 0) # right side red
        else:
            self.get_logger().info("set color to green")
            self.call_setpen_service(0, 255, 0, 3, 0) # left side green
        
    def call_setpen_service(self, r, g, b, width, off):
        client = self.create_client(SetPen, "/turtle1/set_pen")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("waiting for service...")
        request = SetPen.Request()
        request.r  = r
        request.g  = g
        request.b  = b
        request.width  = width
        request.off  = off

        future = client.call_async(request)
        # fixed the param in the function by partial
        # useful in asyn comm when the response not recevied yet
        future.add_done_callback(partial(self.callback_set_pen))


    def callback_set_pen(self, future):
        try:
            response = future.result() # get the response, in this case nothing
        except Exception as e:
            self.get_logger().error("Service call failed: %r" % (e, ))

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()
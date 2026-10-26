#!/usr/bin/env python3

# @author alpogant
# Date: 2022-08-10
# iturover team software subteam assignment part 2 (ROS 2 version)

import binascii
import bz2

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Bz2PublisherNode(Node):
    def __init__(self):
        super().__init__("bz2_node")
        self.msg = b'somewhere, something incredible is waiting to be known.'
        self.get_logger().info("BZ2 Compressed Message Publisher Node Started!")
        self.pub = self.create_publisher(String, "/bz2_message", 10)
        self.compress()
        self.timer = self.create_timer(0.2, self.timer_callback)  # 5 Hz

    def compress(self):
        self.compressed_msg = bz2.compress(self.msg)
        self.get_logger().info(str(self.compressed_msg))
        self.compressed_ascii = binascii.hexlify(self.compressed_msg).decode("ascii")
        self.get_logger().info(self.compressed_ascii)

    def timer_callback(self):
        pubm = String()
        pubm.data = self.compressed_ascii
        self.pub.publish(pubm)


def main(args=None):
    rclpy.init(args=args)
    node = Bz2PublisherNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()

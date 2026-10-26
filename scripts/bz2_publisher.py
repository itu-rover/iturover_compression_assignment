#!/usr/bin/env python

# @author alpogant
# Date: 2022-08-10
# iturover team software subteam assignment part 2

import rospy
from std_msgs.msg import String
import bz2
import binascii

class msg_class:
    def __init__(self):
        rospy.init_node("bz2_node", anonymous=False)
        self.init()
        self.compress()
        self.run()

    def init(self):
        self.msg = b'somewhere, something incredible is waiting to be known.'
        rospy.loginfo("BZ2 Compressed Message Publisher Node Started!")
        self.pub = rospy.Publisher("/bz2_message", String, queue_size=10)
        self.rate = rospy.Rate(5)

    def compress(self):
        self.compressed_msg = bz2.compress(self.msg)
        rospy.loginfo(self.compressed_msg)
        self.compressed_ascii = binascii.hexlify(self.compressed_msg).decode("ascii")
        rospy.loginfo(self.compressed_ascii)

    def run(self):
        while not rospy.is_shutdown():
            self.pubm = String()
            self.pubm.data = self.compressed_ascii
            self.pub.publish(self.pubm)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        msg_class()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python3

import rospy
from std_msgs.msg import String 


if __name__=='__main__':
    rospy.init_node('publisher.py', anonymous=True)
    pub = rospy.Publisher("chatter",String,queue_size=10)
    rate = rospy.Rate(10)
    count = 0
    while not rospy.is_shutdown():
        msg = "hello this is working %d" % count
        pub.publish(msg)
        rate.sleep()
        count +=1

 
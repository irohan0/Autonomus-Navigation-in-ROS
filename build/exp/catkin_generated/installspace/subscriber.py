#!/usr/bin/env python3

import rospy
from std_msgs.msg import String 

def msgCallback(msg):
    rospy.loginfo("New message %s" , msg.data)

if __name__== '__main__':
    rospy.init_node("subscriber", anonymous=True)
    rospy.Subscriber("chatter", String, msgCallback)

    rospy.spin()
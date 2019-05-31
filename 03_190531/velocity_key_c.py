#!/usr/bin/env python
# license removed for brevity
import rospy
import roslib
from geometry_msgs.msg import Twist
import cv2

def talker():
    pub = rospy.Publisher('/hsrb/command_velocity', Twist, queue_size=10)
    rospy.init_node('velocity_key', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    image = cv2.imread(roslib.packages.get_pkg_dir('lecture_pkg') + '/files/InputKey.png')
    cv2.imshow('InputWindow',image)

    while not rospy.is_shutdown():

        key = cv2.waitKey(1)
        rospy.loginfo(key)
        command = Twist()
        if key == 119: # w
          command.linear.x  =  1
          command.linear.y  =  0
          command.angular.z =  0
        if key == 97: # a
          command.linear.x  =  0
          command.linear.y  =  0
          command.angular.z =  1
        if key == 115: # s
          command.linear.x  = -1
          command.linear.y  =  0
          command.angular.z =  0
        if key == 100: # d
          command.linear.x  =  0
          command.linear.y  =  0
          command.angular.z = -1
        if key == 113: #q
          command.linear.x  =  0
          command.linear.y  =  0
          command.angular.z =  0
        if key == 27: #esc
          rospy.loginfo("EXIT")
          break
        rospy.loginfo(command)
        pub.publish(command)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except:
        print("ERROR")
        pass

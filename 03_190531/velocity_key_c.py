#!/usr/bin/env python
# license removed for brevity
import rospy
import roslib
import cv2

if __name__ == '__main__':
  rospy.init_node('velocity_key_c')
  image = cv2.imread(roslib.packages.get_pkg_dir('lecture_pkg') + '/files/InputKey.png')
  cv2.imshow('InputWindow',image)
  r = rospy.Rate(10)
  while not rospy.is_shutdown():
    key = cv2.waitKey(1)
    print(key)
    rospy.loginfo(key)
    r.sleep()
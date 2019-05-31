
import cv2

image = cv2.imread(roslib.packages.get_pkg_dir('lecture_pkg') + '/files/InputKey.png')
cv2.imshow('InputWindow',image)

key = cv2.waitKey(1)
rospy.loginfo(key)
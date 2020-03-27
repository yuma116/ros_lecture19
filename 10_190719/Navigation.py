#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import *

if __name__ == "__main__" :
  try :
    rospy.init_node("send_goal")
    client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.stamp    = rospy.Time.now()
    goal.target_pose.header.frame_id = "/map"
    goal.target_pose.pose.position.x = 0.00 #0.12
    goal.target_pose.pose.position.y = 0.48 #0.46
    goal.target_pose.pose.orientation.w = 0.01
    print goal
    client.send_goal(goal)
    print client.wait_for_result()
  except rospy.ROSInterruptException: pass
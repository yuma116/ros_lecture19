#!/usr/bin/env python  
import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('tf_listener')

    listener = tf.TransformListener()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/link1', '/link2', rospy.Time(0))
            euler = tf.transformations.euler_from_quaternion(rot)
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        print("--trans--")
        print(trans)
        print("--euler--")
        print(euler)
        print("=========")
        rate.sleep()
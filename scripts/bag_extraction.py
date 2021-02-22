#!/usr/bin/env python
import rosbag
import rospy
from nav_msgs.msg import Odometry
# from nav_msgs import Odometry

bag = rosbag.Bag('/home/gryogor/to_test.bag')

for topic, msg, t in bag.read_messages(topics='/robotont/odom'):
    print(msg.pose.pose.position)
bag.close()

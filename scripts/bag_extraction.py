#!/usr/bin/env python
import rosbag
import rospy
from nav_msgs.msg import Odometry
import pandas as pd
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from geometry_msgs.msg import Quaternion
# from nav_msgs import Odometry

bagfile = '/home/gryogor/to_test.bag'
filename = "/home/gryogor/positions.csv"

bag = rosbag.Bag(bagfile)

columns = ['position x', 'position y', 'yaw', 'time']

df = pd.DataFrame(columns=columns)

for topic, msg, t in bag.read_messages(topics='/robotont/odom'):
    quaternion = (
    msg.pose.pose.orientation.x,
    msg.pose.pose.orientation.y,
    msg.pose.pose.orientation.z,
    msg.pose.pose.orientation.w)
    (roll, pitch, yaw) = euler_from_quaternion(quaternion)
    a = [[msg.pose.pose.position.x, msg.pose.pose.position.y, yaw, msg.header.stamp.secs+msg.header.stamp.nsecs*10**-9]]
    df2 = pd.DataFrame(a, columns=columns)
    df = df.append(df2)

df.to_csv(filename,index=False)
bag.close()

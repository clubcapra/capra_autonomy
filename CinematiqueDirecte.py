#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


def avancer(x) :

    Twist.linear.x = x
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    return


def tourner(Rz) :

    Twist.angular.z = Rz
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    return


def arreter() :

    Twist.linear.x = 0
    Twist.angular.z = 0
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    return

    
#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


def avancer(x)

    twist = x
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    return


def tourner(Rz)

    twist = Rz
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    return


def arreter()

    twist = 0
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    return

    
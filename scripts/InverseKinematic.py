#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
#max linear speed = 1.5 m/s
#max angular speed = 4 rad/s
LINEAR_SPEED=1.0
ANGULAR_SPEED=1.0

move = Twist() # defining the way we can allocate the values


def kinematic() :

    move.linear.x = 1.0 # allocating the values in x direction - linear
    move.angular.z = 1.0  # allocating the values in z direction - angular
    move_pub = rospy.Publisher('/turtle1/cmd_vel', move, queue_size=1) 
    move_pub.publish()

    return


def arreter() :

    move.linear.x = 0.0 # allocating the values in x direction - linear
    move.angular.z = 0.0  # allocating the values in z direction - angular
    kinematic()

    return


def bouger(Vx,Rz,t) :

    move.linear.x = 1.0 # allocating the values in x direction - linear
    move.angular.z = 1.0  # allocating the values in z direction - angular
    kinematic()
    rospy.sleep(t)
    arreter()

    return


def avancer(t) :

    bouger(LINEAR_SPEED,0,t)
    rospy.sleep(t)
    arreter()

    return


def tourner(t) :
    
    bouger(0,ANGULAR_SPEED,t)
    rospy.sleep(t)
    arreter()

    return
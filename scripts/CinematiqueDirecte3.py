#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
#max linear speed = 1.5 m/s
#max angular speed = 4 rad/s
LINEAR_SPEED=1
ANGULAR_SPEED=1

rospy.init_node('direct_kinematic', anonymous=True)
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)

move = Twist() # defining the way we can allocate the values
move.linear.x = 0.5 # allocating the values in x direction - linear
move.angular.z = 0.5  # allocating the values in z direction - angular

def kinematic() :

    while not rospy.is_shutdown():

        pub.publish(move)
        rate.sleep()

    return

def arreter() :

    #publish Vx et Rz to cmd vel with twist message
    move.linear.x = 0 # allocating the values in x direction - linear
    move.angular.z = 0  # allocating the values in z direction - angular
    kinematic()

    return


def bouger(Vx,Rz,t) :

    move.linear.x = Vx # allocating the values in x direction - linear
    move.angular.z = Rz  # allocating the values in z direction - angular
    rospy.sleep(t)
    arreter()
    kinematic()

    return


def avancer(t) :

    bouger(LINEAR_SPEED,0,t)

    return


def tourner(t) :
    
    bouger(0,ANGULAR_SPEED,t)

    return


rostopic pub -r 1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'
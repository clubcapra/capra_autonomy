#vitesse lineaire max = 1.5 m/s
#vitesse angulaire max = 4 rad/s

#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def kinematic() :

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('direct_kinematic', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():

        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

    return

def arreter() :

    #publier Vx et Rz cmd vel un twist message avec des 0
    msg = Twist()
    Twist.linear.x = 0
    Twist.angular.z = 0
    kinematic()

    return


def bouger(Vx,Rz,t) :

    T0 = rospy.get_time()

    while (Tf - T0) > t :

        #publier Vx et Rz cmd vel un twist message
        Twist.linear.x = Vx
        Twist.angular.z = Rz
        node()
        Tf = rospy.get_time()

    arreter()
    kinematic()

    return


def avancer(Vx,t) :

    bouger(Vx,0,t)

    return


def tourner(Rz,t) :
    
    bouger(0,Rz,t)

    return



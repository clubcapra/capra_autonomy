#vitesse lineaire max = 1.5 m/s
#vitesse angulaire max = 4 rad/s

#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def arreter() :

    #publier Vx et Rz cmd vel un twist message avec des 0
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    return


def avancer(Vx,t) :

    while t < T :

        #publier Vx à cmd vel un twist message
        Twist.angular.x = Vx
        pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    arreter()

    return


def tourner(Rz,t) :
    
    while t < T :

        #publier Rz à cmd vel un twist message
        Twist.angular.z = Rz
        pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    arreter()

    return


def cercle(Vx,Rz) :

    #publier Vx et Rz cmd vel un twist message
    Twist.angular.x = Vx
    Twist.angular.z = Rz
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    return
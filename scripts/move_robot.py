#import CinematiqueDirecte
import rospy
from geometry_msgs.msg import Twist

def kinematic() :

    move = Twist() # defining the way we can allocate the values
    move.linear.x = 1.0 # allocating the values in x direction - linear
    move.angular.z = 1.0  # allocating the values in z direction - angular
    move_pub = rospy.Publisher('/turtle1/cmd_vel', move, queue_size=1) 
    move_pub.publish()

    return

kinematic()
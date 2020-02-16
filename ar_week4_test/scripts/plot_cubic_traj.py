#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from ar_week4_test.msg import *
from ar_week4_test.srv import *

def callback(data):
 #Get the value from the message
 a0=data.a0
 a1=data.a1
 a2=data.a2
 a3=data.a3
 t0=data.t0
 tf=data.tf
 #Initialize t
 t = 0
 # calculation position, velocity and acceleration.
 while t<tf:
	       
 	position=a0+(a1*t)+(a2*t**2)+(a3*t**3)
	speed=a1+(2*a2*t)+(3*a3*t**2)
 	acce=2*a2+6*a3*t
	#Give call the talker function to publish these three value
        talker(position,speed,acce)
        t=t+0.001
        
def listener():
    #Initialize the node name
    rospy.init_node('plot_cubic_traj', anonymous=True)
     #Declare the node subscriber the "cubic_traj_coeffs" topic using the cubic_traj_coeffs   message type
    rospy.Subscriber("cubic_traj_coeffs", cubic_traj_coeffs, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def talker(position,speed,acce):

    #Initialize there Publishers and using Float32 message type 
    pub = rospy.Publisher('position_trajectory',Float32,queue_size=10)
    pub1 = rospy.Publisher('velocity_trajectory',Float32,queue_size=10)
    pub2 = rospy.Publisher('acceleration_trajectory',Float32, queue_size=10)
    #Publish these three topics
    pub.publish(position)
    pub1.publish(speed)
    pub2.publish(acce)
    #rate.sleep()
if __name__ == '__main__':
    listener()

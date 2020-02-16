#!/usr/bin/env python
import rospy
import random
#from std_msgs.msg import Float32
from ar_week4_test.msg import cubic_traj_params  #import the msg file from package

# Define the Talker function

def talker():
    #Declare the node is publishing to the cubic_traj_params topic using the cubic_traj_params   message type
    pub = rospy.Publisher('cubic_traj_params', cubic_traj_params, queue_size=10)
    #Initialize the node name
    rospy.init_node('points_generator', anonymous=True)
    #Creates a Rate object rate,With the help of its method sleep()
    rate = rospy.Rate(0.05) # 20secs
    #a loop  to generator six random value every 20 secs and publish by using random.uniform() and rate.sleep()
    while not rospy.is_shutdown():
	dt = random.uniform(5,10)
	p0 = random.uniform(-10,10)
	pf = random.uniform(-10,10)
	v0 = random.uniform(-10,10)
	vf = random.uniform(-10,10)
	t0 = (0)
	tf = (dt)
        pub.publish(p0,pf,v0,vf,t0,tf)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

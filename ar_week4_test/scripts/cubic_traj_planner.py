#!/usr/bin/env python
import rospy
import random
#from std_msgs.msg import String
from ar_week4_test.msg import *   #import the msg file from package
from ar_week4_test.srv import *   #import the srv file from package

def callback(data):
    #Give the value to the service message
    msg1 = compute_cubic_traj()
    msg1.p0 = data.p0
    msg1.pf = data.pf
    msg1.v0 = data.v0
    msg1.vf = data.vf
    msg1.t0 = data.t0
    msg1.tf = data.tf
    #call the compute_cubic_coeffs_client function and renturn the coefficents values
    coeff=compute_cubic_coeffs_client(msg1)
    talker(coeff,msg1)
    
    
def listener():
    #Initialize the node name
    rospy.init_node('cubic_traj_planner', anonymous=True)
    #Declare the node subscriber the "cubic_traj_params" topic using the cubic_traj_params   message type
    rospy.Subscriber("cubic_traj_params", cubic_traj_params, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def talker(coeff,msg1):
    #Declare the node is publishing to the "cubic_traj_coeffs" topic using the cubic_traj_coeffs   message type
    pub = rospy.Publisher('cubic_traj_coeffs', cubic_traj_coeffs, queue_size=10)
    #Get value from the coeff 
    a0 = coeff.a0
    a1 = coeff.a1
    a2 = coeff.a2
    a3 = coeff.a3
    t0 = msg1.t0
    tf = msg1.tf
    #Publish the data
    pub.publish(a0,a1,a2,a3,t0,tf)


def compute_cubic_coeffs_client(req):
    #Blocks until the service named compute_cubic_traj is available
    rospy.wait_for_service('compute_cubic_traj')
    try:
	#create a handle for calling the service
        Compute_cubic_traj = rospy.ServiceProxy('compute_cubic_traj', compute_cubic_traj)
	resp1 = Compute_cubic_traj(req.p0,req.pf,req.v0,req.vf,req.t0,req.tf)
	print('get answer')        
	return resp1
    except rospy.ServiceException, e:
        print("Service call failed: %s"%e)

if __name__ == '__main__':
    listener()

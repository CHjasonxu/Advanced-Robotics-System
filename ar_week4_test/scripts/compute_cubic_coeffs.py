#!/usr/bin/env python
from ar_week4_test.srv import *
import rospy
import numpy as np

def handle_compute_cubic_coeffs(req):
    #Get the value from req data
    p0 = req.p0
    pf = req.pf
    v0 = req.v0
    vf = req.vf
    t0 = req.t0
    tf = req.tf
    # set the M matrix
    M = np.array([[1,t0,t0**2,t0**3],
                  [0,1,2*t0,3*t0**2],
                  [1,tf,tf**2,tf**3],
                  [0,1,2*tf,3*tf**2]])
    # set the c matrix
    c = np.array([[p0],[v0],[pf],[vf]])
    # using the equation from leacture----M * c = a , and using linear algebra to get a matrix
    a = np.linalg.inv(M).dot(c)
    print(a)
    return compute_cubic_trajResponse(a[0][0],a[1][0],a[2][0],a[3][0])

def compute_cubic_coeffs_server():
    #Initialize the node name
    rospy.init_node('compute_cubic_coeffs', anonymous=True)

    #This declares a new service named compute_cubic_traj with the compute_cubic_traj service type. All requests are passed to handle_compute_cubic_coeffs function. handle_compute_cubic_coeffs is called with instances of compute_cubic_trajRequest and returns instances of compute_cubic_trajResponse. 
    s = rospy.Service('compute_cubic_traj', compute_cubic_traj, handle_compute_cubic_coeffs)
    rospy.spin()

if __name__ == "__main__":
    compute_cubic_coeffs_server() 

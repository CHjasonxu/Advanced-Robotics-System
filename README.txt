


First Step: Extract the 190622114_ar_week4_test.zip file. This file contains package,video and README file.

Second Step: Put the package(ar_week4_test) in the /catkin_ws/src

Thrid Step: Buliding the package, using the command (catkin_make) in the terminalros. the path should be  /catkin_ws.

Fourth Step: using the roslaunch to run the code. please use this command: roslaunch ar_week4_test cubic_traj_gen.launch.

Note: 

i set the dealy for rqt_plot in launch file. So when you roslaunch the launch file,you need wait 25 secs to get the rqt_plot GUI.And you also need wait 20-40 secs to plot data.

For the rqt_graph, when the rqt_plot works, you can refresh rqt-graph(the blue button on the top-left corner).Then you will see all the nodes and topics.

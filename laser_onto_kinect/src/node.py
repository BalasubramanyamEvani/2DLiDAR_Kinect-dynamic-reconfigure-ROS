'''

@Author: Balasubramanyam Evani
Manipal University Jaipur

'''

#!/usr/bin/env python

## Importing necessary libraries

import rospy
from dynamic_reconfigure.server import Server
from laser_onto_kinect.cfg import configConfig
import tf
import math

## class containig methods for implementing dynamic reconfigure and sending the transform
class dynamicTF(object):

		def __init__(self):

			self.parent_name = rospy.get_param('~parent' , 'camera_rgb_frame') ## parameter specifying the parent frame
			self.child_name = rospy.get_param('~child' , 'laser')              ## parameter specifying the child frame
			self.linear = [0 ,0, 0]                                            ## initializing translation 
			self.rot = [0 ,	0, 0]						   ## initializing rotation
			self.br = tf.TransformBroadcaster()				   ## Transform Broadcaster object

		def run(self):								   ## Run at 10Hz
			rospy.Rate(10)
			config = Server(configConfig , self.callback)		           ## dynamic configure callback
			self.send_transform()						   ## sending the tf
			rospy.spin()							   ## stops from exiting

		def callback(self , config , level):
			self.linear = [ float("{x}".format(**config)) , float("{y}".format(**config)) , float("{z}".format(**config))]
			self.rot = [float("{roll}".format(**config)), float("{pitch}".format(**config)), float("{yaw}".format(**config))] 
			return config

		def send_transform(self):
			rospy.Rate(10)
			while not rospy.is_shutdown():

				self.br.sendTransform((self.linear[0] , self.linear[1] , self.linear[2]), tf.transformations.quaternion_from_euler(self.rot[0] * math.pi/180.0 , self.rot[1] * math.pi/180.0 ,self.rot[2]* math.pi/180.0) , rospy.Time.now() , self.child_name , self.parent_name) ## converting degrees to rads and sendign the tranform b/w parent and child

## Main Function Call

if __name__ == '__main__':
		rospy.init_node("TF_broadcaster" , anonymous = True) ## initialization of node
		TF = dynamicTF() 				     ## Creating object of class dynamicTF
		TF.run()					     ## running the process

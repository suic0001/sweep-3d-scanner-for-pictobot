#! /usr/bin/env python

import rospy
import std_msgs.msg

def pub_ar():

	pub = rospy.Publisher('set_ar', std_msgs.msg.Int32, queue_size=10)
	
	rospy.init_node('pub_ar')
	
	rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		
		print "Default angular scan range is 40 degrees"
		
		try:
		
			angular_range = raw_input("Enter the angular range you want, from 1 to 180(degree)")
			
		except:
		
			angular_range = 40
			
		print "Angular range you set is: "+ str(angular_range)
		
		pub.publish(int(angular_range))
		
		rate.sleep()
		
if __name__ == '__main__':
	try:
		pub_ar()
	except rospy.ROSInterruptException:
		pass

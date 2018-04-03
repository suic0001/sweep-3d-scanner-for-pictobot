#! /usr/bin/env python

import rospy
import std_msgs.msg

def pub_sr():

	pub = rospy.Publisher('set_sr', std_msgs.msg.Int32, queue_size=10)
	
	rospy.init_node('pub_sr')
	
	rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		
		print "Default sample rate is 1000 Hz(just press enter)"
		
		try:
		
			sample_rate = raw_input("Enter the sample rate you want, 500 or 750 or 1000 ")

		except:
		
			sample_rate = 1000
			
		print "Sample rate you set is: "+ str(sample_rate)

		pub.publish(int(sample_rate))
		
		rate.sleep()
		
if __name__ == '__main__':
	try:
		pub_sr()
	except rospy.ROSInterruptException:
		pass

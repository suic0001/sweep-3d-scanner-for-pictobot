#! /usr/bin/env python

import rospy
import std_msgs.msg

def pub_ms():

	pub = rospy.Publisher('set_ms', std_msgs.msg.Int32, queue_size=10)
	
	rospy.init_node('pu_msb')
	
	rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		
		print "Default motor speed is 5 Hz(just press enter)"
		
		try:

			motor_speed = raw_input("Enter the motor speed you want, integer from 1 to 10: ")
				
		except:

			motor_speed = 5
			
		print "Motor speed you set is: "+ str(motor_speed)
		
		pub.publish(int(motor_speed))
		
		rate.sleep()
		
if __name__ == '__main__':
	try:
		pub_ms()
	except rospy.ROSInterruptException:
		pass

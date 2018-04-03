#! /usr/bin/env python
import rospy
import std_msgs.msg

def pub_motor_speed():

	pub = rospy.Publisher('motor_speed_topic',std_msgs.msg.Int32, queue_size=10)
	rospy.init_node('motor_speed_node', anonymous=True)
	rate = rospy.Rate(10)


	while not rospy.is_shutdown():
		print ("Default motor speed would be 5 Hz")
		try:		
			motor_speed = int(raw_input("Enter the speed of motor(Lidar), integer from 1 to 10: "))
		except:
			motor_speed = 5		

		print ("motor speed is: ", motor_speed)
		rospy.loginfo(motor_speed)
		pub.publish(motor_speed)
		rate.sleep()


if __name__ == '__main__':
	try:
		pub_motor_speed()
	except rospy.ROSInterruptException:
		pass



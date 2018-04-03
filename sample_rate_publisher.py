#! /usr/bin/env python
import rospy
import std_msgs.msg

def pub_sample_rate():

	pub = rospy.Publisher('sample_rate_topic',std_msgs.msg.Int32, queue_size=10)
	rospy.init_node('sample_rate_node', anonymous=True)
	rate = rospy.Rate(10)


	while not rospy.is_shutdown():
		print ("Default sample rate would be 1000")
		
		try:
			
			sample_rate = int(raw_input("sample rate = 500 or 750 or just press enter to use default 1000: "))
						
		except:
			sample_rate = 1000
		

		print "Sample rate is: ", sample_rate
		rospy.loginfo(sample_rate)
		print "\n"
		pub.publish(sample_rate)
		rate.sleep()


if __name__ == '__main__':
	try:
		pub_sample_rate()
		
	except KeyboardInterrupt:
		pass



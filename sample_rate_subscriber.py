#! /usr/bin/env python
import rospy
import std_msgs.msg
#import argparse

'''
class subscriber():
	
	sample_rate = 0
	
	motor_speed = 0
		
#	def __init__(self):
#	
#		self.subscriber = rospy.Subscriber("sample_rate_topic", std_msgs.msg.Int32, self.callback)
		
	def sample_rate_callback(self,data1):
		rospy.loginfo("sample_rate is: %d", data1.data)
		sample_rate = data1.data
		#print self.value
		#print "\n"

	def motor_speed_callback(self,data2):
		rospy.loginfo("motor_speed is %d", data2.data)
		motor_speed = data2.data
		
		

'''
motor_speed = None

sample_rate = None

def sample_rate_callback(data):
	global sample_rate
	
	rospy.loginfo("sample_rate is: %d", data.data)
	
	sample_rate = data.data
	
#	parser.add_argument('-sr', '--sample_rate',#ask for sample rate input  --- publisher done
#                        help='Sample Rate(either 500, 750 or 1000)',
#                        #default=sweep_helpers.SAMPLE_RATE_500_HZ,
#                        required=False)


def motor_speed_callback(data):

	global motor_speed
	
	rospy.loginfo("motor_speed is: %d", data.data)
	
	motor_speed = data.data
	
#	parser.add_argument('-ms', '--motor_speed',#ask for motor speed input ----  publisher done
#                        help='Motor Speed (integer from 1:10)',
#                        #default=sweep_helpers.MOTOR_SPEED_1_HZ,
#                        required=False)

def sample_rate_setter():		
	
	rospy.init_node('subscriber', anonymous=True)
	
#	sub_object = subscriber()
	
	
	
	rospy.Subscriber("sample_rate_topic", std_msgs.msg.Int32, sample_rate_callback)
	
	rospy.Subscriber("motor_speed_topic", std_msgs.msg.Int32, motor_speed_callback)

	

#	while not rospy.is_shutdown():

	
#try:	
	
	
	#print "this is in main program, that the smaple rate is: "+ str(sample_rate)
	
#		rospy.loginfo("this is in main program, the sample rate is: %d", int(sample_rate))
	
	#rospy.sleep(1)
	
	
		
	#print "this is also in main program, that the motor speed is: "+ str(motor_speed)
	
#		rospy.loginfo("also in main program, the motor speed is: %d", int(motor_speed))
		
#		rospy.sleep(3.)
		#rospy.spin()
	#try:
	
		
		#rospy.spin()
		
	#except KeyboardInterrupt:
	#	pass	
#except KeyboardInterrupt:
#	pass
'''
def main(arg_dict):

	print "ok1"

	print ("this is in main program", int(arg_dict['motor_speed']))
	print "\n"
	
	print ("this is also in main program" , int(arg_dict['sample_rate']))
	print "\n"

'''



if __name__=='__main__':
	#parser = argparse.ArgumentParser(description='Just to test to save two data from different topic')
	#motor_speed = 0
	
	#sample_rate = 0
	
	sample_rate_setter()
	
	while not rospy.is_shutdown():
		
		print sample_rate
		
		print motor_speed
		
		rospy.sleep(3.)
		#rospy.spin()
	
	#args = parser.parse_args()
	#argsdict = vars(args)
	
	#main(argsdict)
	
	

#! /usr/bin/env python
import sample_rate_subscriber
#import os


sample_rate_setter = sample_rate_subscriber.sample_rate_subscriber

#execfile("~/catkin_ws/src/beginner_tutorials/scripts/sample_rate_subscriber.py")
sample_rate_subscriber.sample_rate_setter()

print "ok1"
print sample_rate_setter.value





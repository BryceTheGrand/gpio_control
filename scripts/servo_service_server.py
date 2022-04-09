#!/usr/bin/env python

import rospy
from gpio_control.srv import SetGPIO
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
p = GPIO.PWM(20, 50)
p.start(2.5)


def set_pin_callback(req):
    rospy.loginfo(req.data)
    p.ChangeDutyCycle(req.value)
    return {
        'res': 'OK'
    }


def main():
    rospy.init_node('servo_service_server')
    rospy.Service('set_gpio_output', SetGPIO, set_pin_callback)
    rospy.loginfo('Server service started. Ready to receive requests.')
    rospy.spin()
    GPIO.cleanup()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        rospy.loginfo('Shutting down server.')
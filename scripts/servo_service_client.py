#!/usr/bin/env python

import rospy
from gpio_control.srv import SetGPIO
from std_msgs.msg import String


def control_gpio(msg):
    rospy.wait_for_service('set_gpio_output')
    rospy.loginfo('Received a message: ' + msg.data)
    if msg.data == "close_servo":
        try:
            set_gpio_output = rospy.ServiceProxy('set_gpio_output', SetGPIO)
            set_gpio_output(20, 5)
        except rospy.ServiceException as e:
            rospy.logwarn(e)
    elif msg.data == "open_servo":
        try:
            set_gpio_output = rospy.ServiceProxy('set_gpio_output', SetGPIO)
            set_gpio_output({
                'pin':   20,
                'value': 12
            })
        except rospy.ServiceException as e:
            rospy.logwarn(e)


def main():
    rospy.init_node('servo_service_client_node')
    gpio_sub = rospy.Subscriber('gpio_msgs', String, control_gpio)
    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        rospy.loginfo('Client died.')

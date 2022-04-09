#!/usr/bin/env python

import rospy
from gpio_control.srv import SetGPIO
from std_msgs.msg import String


def control_gpio(msg):
    rospy.wait_for_service('set_gpio_output')
    if msg.data == "close_servo":
        try:
            set_gpio_output = rospy.ServiceProxy('set_gpio_output', SetGPIO)
            set_gpio_output({
                'pin':   20,
                'value': 100
            })
        except rospy.ServiceException:
            rospy.logwarn("Exception processing")
    elif msg.data == "open_servo":
        pass


def main():
    rospy.init_node('servo_service_client_node')
    rospy.Subscriber('gpio_msgs', String)


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        rospy.loginfo('Client died.')

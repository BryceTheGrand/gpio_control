#!/usr/bin/env python

import rospy
from gpio_control.srv import SetGPIO
from std_msgs.msg import String


set_gpio_output = None


def control_gpio(msg):
    global set_gpio_output
    rospy.wait_for_service('set_gpio_output')
    rospy.loginfo('Received a message: ' + msg.data)
    if msg.data == "close_servo":
        try:
            for i in range(20):
                set_gpio_output(20, 2 + (i + 1) * 0.25)
                rospy.sleep(2 / 20)
        except rospy.ServiceException as e:
            rospy.logwarn(e)
    elif msg.data == "open_servo":
        try:
            set_gpio_output(20, 2)
        except rospy.ServiceException as e:
            rospy.logwarn(e)


def main():
    rospy.init_node('servo_service_client_node')
    gpio_sub = rospy.Subscriber('gpio_msgs', String, control_gpio)
    global set_gpio_output
    set_gpio_output = rospy.ServiceProxy('set_gpio_output', SetGPIO)
    rospy.wait_for_service('set_gpio_output')
    set_gpio_output(20, 2)
    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        rospy.loginfo('Client died.')

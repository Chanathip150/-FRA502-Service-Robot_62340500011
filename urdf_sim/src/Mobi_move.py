#!/usr/bin/env python3
import rospy
import speech_recognition as sr
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point
import time
# this method will make the robot move to the goal location
def move_to_goal(xGoal, yGoal,angle):
    # define a client for to send goal requests to the move_base server through a SimpleActionClient
    ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

    # wait for the action server to come up
    while (not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
        rospy.loginfo("Waiting for the move_base action server to come up")

    goal = MoveBaseGoal()

    # set up the frame parameters
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    # moving towards the goal*/

    goal.target_pose.pose.position = Point(xGoal, yGoal, 0)
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = angle
    goal.target_pose.pose.orientation.w = 1.0

    rospy.loginfo("Sending goal location ...")
    ac.send_goal(goal)

    ac.wait_for_result(rospy.Duration(120))

    if (ac.get_state() == GoalStatus.SUCCEEDED):
        rospy.loginfo("You have reached the destination")
        return True

    else:
        rospy.loginfo("The robot failed to reach the destination")
        return False


if __name__ == '__main__':
    rospy.init_node('map_navigation', anonymous=False)
    x_goal1 = 0.438028
    x_goal2 = 14.035000
    x_goal3 = 13.1472000
    x_goal4 = 4.402180
    x_goalh = 1.108787
    x_goal5 = 7.593530
    y_goal1 = 3.516360
    y_goal2 = 3.769300
    y_goal3 =6.210090
    y_goal4 = 8.248320
    y_goalh = -0.062583
    y_goal5 = 15.795300
    angle1 = 0
    angle2 = 0
    angle3 = 0
    angleh = -0.001
    angle4 =0
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print(source)
        print("start")
        # playsound("signal.mp3")
        audio = r.record(source, duration=5)  # บันทึกเสียง 5 วินาท
        # print(type(audio))# ี
        print("finish")
        # playsound("signal.mp3")
        # print(audio)
    try:
        text = r.recognize_google(audio, language = 'en')
        print(text)
    except:
        text = "Try again please"
    if "a" in text:
        move_to_goal(x_goal1, y_goal1,angle1)
        print('room 1')
        move_to_goal(x_goalh, y_goalh, angleh)
        print('Success')
    if "B" in text or "b" in text:
        move_to_goal(x_goal2, y_goal2,angle2)
        print('room 2')
        move_to_goal(x_goalh, y_goalh, angleh)
        print('Success')
    if "C" in text or"c" in  text:
        move_to_goal(x_goal3, y_goal3,angle3)
        print('room 3')
        move_to_goal(x_goalh, y_goalh, angleh)
        print('Success')
    if "d" in text:
        move_to_goal(x_goal4, y_goal4,angle1)
        print('room 4')
        move_to_goal(x_goalh, y_goalh, angleh)
        print('Success')
    if "f" in text:
        move_to_goal(x_goal5, y_goal5,angle5)
        print('room 5')
        move_to_goal(x_goalh, y_goalh, angleh)
        print('Success')

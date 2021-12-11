#!/usr/bin/env python3

import rospy
import pyaudio
import time
import speech_recognition as sr

# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

r = sr.Recognizer()
cafebot_state = 3


KeyWord = {"go good":"room1",
            "two":"room2",
            "three":"room3",
            "four":"room4",
            "five":"room5",
            "six":"room6",
            "room by":"Standby_Station"          
            }



Goal = {"room1":[0.438028,3.516360,0,0.7511],
        "room2":[14.035000,3.769300,0,0.7511],
        "room3":[13.1472000,6.210090,0,0.7511],
        "room4":[4.402180,8.248320,0,0.7511],
        "room5":[7.593530,15.795300,0,0.7511],
        "room6":[10.147000,13.793300,0,0.7511],
        
        "Standby_Station":[1.108787,-0.062583,-0,0.7511]}




def movebase_client(map_odom_desire):

   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position.x = map_odom_desire[0]
    goal.target_pose.pose.position.y = map_odom_desire[1]

    goal.target_pose.pose.orientation.z = map_odom_desire[2]
    goal.target_pose.pose.orientation.w = map_odom_desire[3]

   # Sends the goal to the action server.
    client.send_goal(goal)
   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()
   # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
    # Result of executing the action
        return client.get_result()   

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        
        while 1:
            try:
                rospy.loginfo("Setting MIC: Say Something . . .")
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    word = r.recognize_google(audio)
                    rospy.loginfo("Mic testing . . . STATUS: OK")
                    break

            except:
                rospy.loginfo("Setting MIC: Say Something . . .")



        while 1:
            if (cafebot_state == 0):
               rospy.loginfo("ready to get command")
               cafebot_state = 1

            elif (cafebot_state == 1):  
                try:
                    with sr.Microphone() as source:                
                        audio = r.listen(source)
                        word = r.recognize_google(audio)
                        try:
                            rospy.loginfo("Going to . . . " + KeyWord[word])
                            result = movebase_client(Goal[KeyWord[word]])
                            if result:
                                rospy.loginfo("Arrive at desired room")
                                cafebot_state = 2
                        except:
                            rospy.loginfo("Can't decode your voice, pls say again pls")
                            rospy.loginfo("Command Example : พูดใหม่")
                            pass

                except:
                    pass

            elif (cafebot_state == 2):  
                rospy.loginfo("Wait for interaction . . .")
                time.sleep(10)
                rospy.loginfo("Back to Standby-Station")
                cafebot_state = 3
            
            elif (cafebot_state == 3):
                rospy.loginfo("Going to . . . Standby_Station")
                result = movebase_client(Goal["Standby_Station"])
                if result:
                    rospy.loginfo("Arrive at the Standby-Station")
                    
                    cafebot_state = 0
            




    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")

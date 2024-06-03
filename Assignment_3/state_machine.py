import nao_nocv_2_1 as nao
from naoqi import ALProxy
import time
import keyboard

robot_ip = "192.168.0.116"
port = 9559  # Robot port number
base_dir = "/home/nao/group_09/"

class StateMachine():
    def __init__(self, robot_ip, port, base_dir):
        self.robot_ip = robot_ip
        self.port = port
        self.base_dir = base_dir
        self.dialog_p = ALProxy('ALDialog', self.robot_ip, self.port)
        self.memory_p = ALProxy('ALMemory', self.robot_ip, self.port)
        self.dialog_p.setLanguage("English")
        self.topics = []
        print("Setup the robot")

#####################################################################################################
        self.current_state_active = None # 1 Roaminig, 2 Detected Visitor, 3 Interacting with user...
        self.state_dict = {1: "Roaming State", 2: "Detected Visitor State", 3: "Interacting with User State", 4: "Moving with Visitor", 5: "Ending Interaction"}

    def get_key_from_value(self, target_value):
        for key, value in self.current_state_active.items():
            if value == target_value:
                return key
        return None

    def states_veerman(self):    # Veerman is a PSV player who dictates the plays
        while True:
            if self.current_state_active == 1:
                next_move, info_for_next_move = self.State_Roaming(info_for_next_move)
            
            if self.current_state_active == 2:
                next_move, info_for_next_move = self.State_Detected_Visitor(info_for_next_move)

            if self.current_state_active == 3:
                next_move, info_for_next_move = self.State_Interacting_User(info_for_next_move)
            self.current_state_active = self.get_key_from_value(next_move)


    def State_Roaming(self, info_for_next_move):
        # Logic that makes the Robot does brr
        face_detected, timestamp, location, face_info = nao.DetectFace() #for nao_nocv_2_1
        if face_detected:
            return "Detected Visitor State" , "Eye contact"
        question_asked, question= self.question_detected()
        if question_asked:
            return "Interacting with User State", question
    

    def State_Detected_Visitor(self):
        face_detected, timestamp, location, face_info = nao.DetectFace() #for nao_nocv_2_1
        if face_detected:
            start_time = time.time()
        else:
            return "Roaming State"
        waiting = True
        face_detected = False
        bool_question_detected = False
        while waiting:
            if time.time() - start_time < 5:
                waiting = False
            elif time.time() - start_time < 2:
                self.tablet_show_image("Smiley")
            question_detected, question = self.question_detected()
            if question_detected:
                waiting = False
            

        face_detected, timestamp, location, face_info = nao.DetectFace()
        if question_detected:
            # A specific question is asked
            return "Interacting with User State", question
        elif face_detected:
            # Turn to question
            # "Hello my name is Eve! Welcome to our museum! You can ask me questions about museum pieces and museum utilities (?)"
            return "Interacting with User State", "Introduce"        
        else:
            return "Roaming State", "Nothing" # No visitor and no question
            
        
    def question_detected(self):
        # Logic question detected
        # if question_detected: THIS ONLY WHEN THERES A DIRECT QUESTION ABOUT THE MUSEUM
        #     return True
        # else:
        #     return False

    def tablet_show_image(self, image_path):
        # Logic to show image on the tablet
        # tabletService = ALProxy("ALTabletService", self.robot_ip, self.port)
        # tabletService.showImageNoCache(image_path)


    def State_Interacting_User(self, prev_move_info):
        # if prev_move_info == "Introduce":
        #     # Turn to question
        #     # "Hello my name is Eve! Welcome to our museum! You can ask me questions about museum pieces and museum utilities (?)"
        
        # else:
        #     prev_move_info == The question from prev
    
            




    
###############################################################################################        



    def ActivateTopic(self, topf_path, module_name='MyModule'):
        # Load topic - absolute path is required
        topf_path = topf_path.decode('utf-8')
        topic = self.dialog_p.loadTopic(topf_path.encode('utf-8'))

        # Start dialog
        self.dialog_p.subscribe(module_name)

        # Activate dialog
        self.dialog_p.activateTopic(topic)

        self.topics.append(topic)

        return topic

    def DeactivateTopic(self, topic, module_name='MyModule'):
        # Deactivate topic
        self.dialog_p.deactivateTopic(topic)

        # Unload topic
        self.dialog_p.unloadTopic(topic)

        # Stop dialog
        self.dialog_p.unsubscribe(module_name)

    def DoStateInit(self):
        print("State: Initial")

        # mylib.InitRobot()
        return "Roaming"

    def StateRoaming(self, mystate):
        print("State: Roaming")

        if mystate == "My state A":
            mylib.behaviourA()
            pass
        elif mystate == "My state B":
            pass
        return "done"

    def StateDetectedVisitor(self, mystate):
        print("State: Detected visitor")

        topf_path = base_dir + "greeting_enu.top"
        topic = self.ActivateTopic(topf_path)


        self.DeactivateTopic(topic)
        return "Roaming"
 

    def StateInteracting(self, mystate):
        print("State: Interacting with visitor")

        topf_path = base_dir + "PracticalQuestion_enu.top"
        topic = self.ActivateTopic(topf_path)

        moving_trigerred = self.memory_p.getData("Move")
        print(moving_trigerred)

        while moving_trigerred != 0:
            moving_trigerred = self.memory_p.getData("Move")
            time.sleep(0.5)  # Check every 500 ms    
        
        # If no more interaction, move to other state of roaming around again
        self.DeactivateTopic(topic)
        if moving_trigerred:
            return "Moving with visitor"
        else:
            return "Roaming"

    def StateMovingVisitor(self, mystate):
        print("State: Moving with visitor")

        return "Done"

    # Main
    def main(self):
        # Initial state
        state = "Interacting"

        while True:
            # Check if 'q' key is pressed
            if keyboard.is_pressed('q'):
                print("You pressed 'q'. Exiting the program. And shutting down topics")
                
                #Stop topics
                for topic in self.topics:
                    self.DeactivateTopic(topic)
                break
            

            # while state != "Done":
                
            #     # last_command = self.memory_p.getData("Dialog/LatestCommand")

            #     if state == "Roaming":
            #         state = self.StateRoaming(state)
            #     elif state == "Detected visitor":
            #         state = self.StateDetectedVisitor(state)
            #     elif state == "Interacting":
            #         state = self.StateInteracting(state)
            #     elif state == "Moving with visitor":
            #         state = self.StateMovingVisitor(state)
            

if __name__ == "__main__":
    sm = StateMachine(robot_ip, port, base_dir)
    sm.main()
    print("Quit the program")

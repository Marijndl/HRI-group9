import nao_nocv_2_1 as nao
from naoqi import ALProxy
import time
import keyboard

robot_ip = "192.168.0.105" # Robot internet address
port = 9559  # Robot port number
base_dir = "/home/nao/group_09/"

class StateMachine():
    def __init__(self, robot_ip, port, base_dir):
        self.robot_ip = robot_ip
        self.port = port
        self.base_dir = base_dir
        self.dialog_p = ALProxy('ALDialog', self.robot_ip, self.port)
        self.memory_p = ALProxy('ALMemory', self.robot_ip, self.port)
        # nao.InitProxy(IP=self.robot_ip, proxy=[1,2,3,5,9], PORT = self.port)  
        nao.InitProxy(IP=self.robot_ip)      
        self.dialog_p.setLanguage("English")
        self.topics = []
        self.gestures = nao.GetAvailableGestures()
        print("Setup the robot")

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


        time.sleep(3)
        return "Done"

    def StateDetectedVisitor(self, mystate):
        print("State: Detected visitor")
    
        face_detected, timestamp, location = nao.DetectFace() # Face detecting
        time.sleep(1)
 
        waiting = True
        activate_hello = True
        start_time = time.time()    
        while waiting:
            if (time.time() - start_time) > 4:
                waiting = False
            elif (time.time() - start_time) > 2:
                if face_detected:
                    if activate_hello:
                        nao.Say("Hello!")
                        activate_hello = False
                    nao.EyeLED([0,0,255])           # For now the eyes will light up
 
        #If a face is still detected, move to interacting state
        if not face_detected:
            face_detected, timestamp, location = nao.DetectFace()
        time.sleep(2)

        if face_detected:
            print("Interacting ")
            nao.EyeLED([0,0,255])
            
            return "Interacting"
        else:
            nao.EyeLED([255,255,255])
            # self.DeactivateTopic(topic)
            return "Roaming"
 

    def StateInteracting(self, mystate):
        print("State: Interacting with visitor")

        #Load topic file
        topf_path = base_dir + "PracticalQuestion_enu.top"
        topic = self.ActivateTopic(topf_path)
        
        #Setting all triggers to zero
        moving_trigerred = 0
        time_gesture = 0
        bathroom_gesture = 0
        nod_gesture = 0
        self.memory_p.insertData('Move','0')
        self.memory_p.insertData('Time','0')
        self.memory_p.insertData('Bathroom','0')
        self.memory_p.insertData('Nod','0')
        print(self.memory_p.getData('Move'))

        # Stay in while loop until next state is triggered
        while str(moving_trigerred) == '0':
            try:
                #Check for trigger variables in memory
                moving_trigerred = self.memory_p.getData('Move')
                time_gesture = self.memory_p.getData('Time')
                bathroom_gesture = self.memory_p.getData('Bathroom')
                nod_gesture = self.memory_p.getData('Nod')
            except:
                moving_trigerred = 0
                time_gesture = 0
                bathroom_gesture = 0
                nod_gesture = 0

            #If triggered, run gestures
            if str(time_gesture) == '1':
                time_gesture = 0
                self.memory_p.insertData('Time','0')
                nao.RunMovement('CheckTime.py')
                time.sleep(5)

            elif str(bathroom_gesture) == '1':
                bathroom_gesture = 0
                self.memory_p.insertData('Bathroom','0')
                nao.RunMovement('Bathroom.py')
                time.sleep(5)
            
            elif str(nod_gesture) == '1':
                nod_gesture = 0
                self.memory_p.insertData('Nod','0')
                nao.RunMovement('Nod.py')
                time.sleep(5)
                print(nod_gesture) 


            # Needed to avoid double animations
            time_gesture = 0
            bathroom_gesture = 0
            nod_gesture = 0
            self.memory_p.insertData('Time','0')
            self.memory_p.insertData('Bathroom','0')
            self.memory_p.insertData('Nod','0')
            time.sleep(0.5)  # Check every 500 ms   
        
        # If no more interaction, move to other state of roaming around again
        time.sleep(2)
        self.DeactivateTopic(topic)
        if str(moving_trigerred) == '1':
            return "Moving with visitor"
        else:
            return "Roaming"

    def StateMovingVisitor(self, mystate):
        print("State: Moving with visitor")

        #Load topic file
        topf_path = base_dir + "Painting_enu.top"
        topic = self.ActivateTopic(topf_path)

        #Introduce topic:
        nao.Say("What painting do you want information on? The one on Van Gogh or the one on PSV?   ", POST=False)

        start = time.time()

        #Set triggers to zero
        painting_trigerred = 0
        self.memory_p.insertData('Painting','0')
        print(self.memory_p.getData('Painting'))

        # Stay in while until painting is mentioned
        while str(painting_trigerred) == "0":
            #Update states
            try:
                painting_trigerred = self.memory_p.getData("Painting")
                print(painting_trigerred)
            except:
                painting_trigerred = 0
            time.sleep(0.5)  # Check every 500 ms 
        
        print(painting_trigerred)
        time.sleep(2)
        self.DeactivateTopic(topic)

        ### Painting scenarios:
        if str(painting_trigerred).lower() == "psv":
            #TODO: movement
            topf_path_psv = base_dir + "PSV_enu.top"
            topic = self.ActivateTopic(topf_path_psv)

            #Start topic:
            # nao.Say("On May 25, 1988, PSV won the European Cup I in Stuttgart after a thrilling final against Benfica, which was decided by penalties. Goalkeeper Hans van Breukelen played the heros role by saving the final penalty from Antonio Veloso, securing PSV their first European Cup victory in the clubs history. Do you want more information on the painting or would you like to continue?")
            nao.Say("Here you can see a painting of the European journey of PSV. The 1988 PSV European journey was rocky. PSV won the quarter and semi finals on away goals against Bordeaux and Real Mardrid. In Suttgart it faced Benfica in the finale. After extra time there were still no goals scored which led to penalties. The penalty phase was tense but Van Breukelen stopped Benfica's 6th penalty causing PSV to win the European Cup One, which is the Champions League today.")
            # nao.RunMovement('PSV.py')


        elif str(painting_trigerred).lower() == "van_gogh":
            #TODO: movement
            topf_path_vangogh = base_dir + "vanGogh_enu.top"
            topic = self.ActivateTopic(topf_path_vangogh)

            #Start topic
            nao.Say("What you see here is the painting The Starry Night by Vincent van Gogh. The starry night, painted in 1889, is one of his most renowned works. The painting depicts a swirling night sky filled with vibrant, expressive stars above a quiet village. Do you want more information on the painting or would you like to continue?")
            nao.RunMovement('vanGogh.py')

            # nao.Say("Yeah")
        else:
            print("We don't have that painting")
            return "Roaming"

        new_painting_trigerred = "-"
        self.memory_p.insertData('Decision','-')
        print(self.memory_p.getData('Decision'))

        while str(new_painting_trigerred).lower() == "-":
            #Update states
            try:
                new_painting_trigerred = self.memory_p.getData("Decision")
            except:
                new_painting_trigerred = "-"
            time.sleep(0.5)  # Check every 500 ms

        print("Decision:" + str(new_painting_trigerred))
        self.DeactivateTopic(topic)
        if str(new_painting_trigerred).lower() == "yes":
            return "Moving with visitor"
        else:
            nao.Say("Thank you for listening, have a nice visit in the museum!")
            time.sleep(2)
            return "Roaming"

    # Main
    def main(self):
        # Initial state
        state = "Detected visitor"

        while True:
            # Check if 'q' key is pressed
            if keyboard.is_pressed('q'):
                print("You pressed 'q'. Exiting the program and shutting down topics")
                
                #Stop topics
                for topic in self.topics:
                    self.DeactivateTopic(topic)
                break
            
            while state != "Done":
                
                # last_command = self.memory_p.getData("Dialog/LatestCommand")

                if state == "Roaming":
                    state = self.StateRoaming(state)
                elif state == "Detected visitor":
                    state = self.StateDetectedVisitor(state)
                elif state == "Interacting":
                    state = self.StateInteracting(state)
                elif state == "Moving with visitor":
                    state = self.StateMovingVisitor(state)

            break
            
            

if __name__ == "__main__":
    sm = StateMachine(robot_ip, port, base_dir)
    sm.main()
    print("Quit the program")

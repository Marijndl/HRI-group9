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
        nao.InitProxy(IP=self.robot_ip, proxy=[1,2,3,9], PORT = self.port)        
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

        topf_path = base_dir + "greeting_enu.top"
        topic = self.ActivateTopic(topf_path)


        self.DeactivateTopic(topic)
        return "Roaming"
 

    def StateInteracting(self, mystate):
        print("State: Interacting with visitor")

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

        start = time.time()

        while str(moving_trigerred) == '0':# and (time.time() - start) < 10:
            try:
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

        topf_path = base_dir + "Painting_enu.top"
        topic = self.ActivateTopic(topf_path)

        #Introduce topic:
        nao.Say("What painting do you want information on?", POST=False)

        start = time.time()

        painting_trigerred = 0
        self.memory_p.insertData('Painting','0')
        print(self.memory_p.getData('Painting'))

        while str(painting_trigerred) == "0":
            #Update states
            try:
                painting_trigerred = self.memory_p.getData("Painting")
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
            nao.Say("On May 25, 1988, PSV won the European Cup I in Stuttgart after a thrilling final against Benfica, which was decided by penalties. Goalkeeper Hans van Breukelen played the heros role by saving the final penalty from Antonio Veloso, securing PSV their first European Cup victory in the clubs history. Do you want more information on the painting or would you like to continue?")

        elif str(painting_trigerred).lower() == "van_gogh":
            #TODO: movement
            topf_path_vangogh = base_dir + "vanGogh_enu.top"
            topic = self.ActivateTopic(topf_path_vangogh)

            #Start topic
            nao.Say("Vincent van Goghs De sterrennacht, The Starry Night, painted in 1889, is one of his most renowned works. The painting depicts a swirling night sky filled with vibrant, expressive stars above a quiet village. Do you want more information on the painting or would you like to continue?")
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
        state = "Interacting"

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

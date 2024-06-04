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
        
        moving_trigerred = 0
        self.memory_p.insertData('Move','0')
        print(self.memory_p.getData('Move'))

        start = time.time()

        while str(moving_trigerred) == '0':# and (time.time() - start) < 10:
            try:
                moving_trigerred = self.memory_p.getData('Move')
            except:
                moving_trigerred = 0
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
        time.sleep(2)

        ### Painting scenarios:
        if str(painting_trigerred).lower() == "psv":
            #TODO: movement
            topf_path_psv = base_dir + "PSV_enu.top"
            topic = self.ActivateTopic(topf_path_psv)

        elif str(painting_trigerred).lower() == "van_gogh":
            #TODO: movement
            topf_path_vangogh = base_dir + "vanGogh_enu.top"
            topic = self.ActivateTopic(topf_path_vangogh)
 
        else:
            print("We don't have that painting")
            return "Roaming"

        new_painting_trigerred = "No decision yet"
        self.memory_p.insertData('Decision','No decision yet')
        print(self.memory_p.getData('Decision'))

        while str(new_painting_trigerred) == "No decision yet":
            #Update states
            try:
                new_painting_trigerred = self.memory_p.getData("Decision")
            except:
                new_painting_trigerred = "No decision yet"
            time.sleep(0.5)  # Check every 500 ms

        self.DeactivateTopic(topic)
        if str(painting_trigerred).lower() == "yes":
            return "Moving with visitor"
        else:
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

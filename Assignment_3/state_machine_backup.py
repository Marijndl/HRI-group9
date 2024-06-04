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

        moving_trigerred = self.memory_p.getData("Move")
        start = time.time()

        while moving_trigerred != 0: # and (time.time() - start) < 10:
            moving_trigerred = self.memory_p.getData("Move")
            time.sleep(0.5)  # Check every 500 ms    
        
        # If no more interaction, move to other state of roaming around again
        self.DeactivateTopic(topic)
        if moving_trigerred == 0:
            return "Moving with visitor"
        else:
            return "Roaming"

    def StateMovingVisitor(self, mystate):
        print("State: Moving with visitor")

        start = time.time()

        psv_trigerred = self.memory_p.getData("psv")
        vang_trigerred = self.memory_p.getData("vangogh")

        while psv_trigerred != 0 and vang_trigerred != 0: #and (time.time() - start) < 10:
            #Update states
            psv_trigerred = self.memory_p.getData("psv")
            vangogh_trigerred = self.memory_p.getData("vangogh")
            time.sleep(0.5)  # Check every 500 ms 

        if psv_trigerred == 0: 
            #TODO: movement
            topf_path_psv = base_dir + "PracticalQuestion_enu.top"
            # topic = self.ActivateTopic(topf_path_psv)
        elif vangogh_trigerred == 0:
            #TODO: movement
            topf_path_vangogh = base_dir + "PracticalQuestion_enu.top"
            # topic = self.ActivateTopic(topf_path_vangogh)
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

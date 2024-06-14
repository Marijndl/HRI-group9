import nao_nocv_2_1 as nao
from naoqi import ALProxy
import time
# import keyboard
 
robot_ip = "192.168.0.105"
port = 9559  # Robot port number
base_dir = "/home/nao/group_09/"
 
class StateMachine():
    def __init__(self, robot_ip, port, base_dir):
        self.robot_ip = robot_ip
        self.port = port
        self.base_dir = base_dir
       
 
        #nao.InitProxy(robot_ip,[0],port)
        nao.InitProxy(robot_ip)
 
 
        self.dialog_p = ALProxy('ALDialog', self.robot_ip, self.port)
        self.memory_p = ALProxy('ALMemory', self.robot_ip, self.port)
        self.dialog_p.setLanguage("English")
 
   
        # self.tabletProxy = nao.ConnectProxy("ALTabletService", robot_ip, port)
 
        # self.tabletProxy.wakeUp()
        # self.tabletProxy.preLoadImage(base_dir + 'signgrass-smiley.jpg')
        # print(self.tabletProxy.showImage(base_dir + 'signgrass-smiley.jpg'))
 
 
 
 
 
       
 
        self.topics = []
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
 
        if mystate == "My state A":
            mylib.behaviourA()
            pass
        elif mystate == "My state B":
            pass
        return "done"
 
    def StateDetectedVisitor(self, mystate):
        print("State: Detected visitor")
        start_time = None
        # topf_path = base_dir + "greeting_enu.top"
        # topic = self.ActivateTopic(topf_path)
 
        face_detected, timestamp, location = nao.DetectFace() # Face detecting
        if face_detected:
            start_time = time.time()
       
        else:
            while not face_detected:
                face_detected, timestamp, location = nao.DetectFace()
                if face_detected:
                    start_time = time.time()
        print("Face detected")
        # else:
        #     self.DeactivateTopic(topic)
        #     return "Roaming"
        if start_time is None:
            print("No face detected")
            start_time = time.time()
        waiting = True
        face_detected = False
        print(start_time)
        # Check if face is still detected after 5 seconds
        while waiting:
            if (time.time() - start_time) > 5:
                print(time.time() - start_time)
                waiting = False
            elif (time.time() - start_time) > 2:
                # face_detected, timestamp, location = nao.DetectFace()
                # if face_detected:
                nao.EyeLED([0,255,0])           # For now the eyes will lid up
                # print("Eyes green")
                # nao.Say("Hello!")
        print("Waiting done")
 
        face_detected = False
        face_detected, timestamp, location = nao.DetectFace()
        time.sleep(2)
        if face_detected:
            print("Interacting ")
            return "Interacting"
   
        else:
            nao.EyeLED([255,255,255])
            # self.DeactivateTopic(topic)
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
        state = "Detected visitor"
 
        while True:
            a = 1
            # Check if 'q' key is pressed
            # if keyboard.is_pressed('q'):
            #     print("You pressed 'q'. Exiting the program. And shutting down topics")
               
            #     #Stop topics
            #     for topic in self.topics:
            #         self.DeactivateTopic(topic)
            #     break
           
 
            while state != "Done":
               
                # last_command = self.memory_p.getData("Dialog/LatestCommand")
 
                # if state == "Roaming":
                #     state = self.StateRoaming(state)
                if state == "Detected visitor":
                    state = self.StateDetectedVisitor(state)
                # elif state == "Interacting":
                #     state = self.StateInteracting(state)
                # elif state == "Moving with visitor":
                #     state = self.StateMovingVisitor(state)
                break
            break
           
 
if __name__ == "__main__":
    sm = StateMachine(robot_ip, port, base_dir)
    sm.main()
    print("Quit the program")
 
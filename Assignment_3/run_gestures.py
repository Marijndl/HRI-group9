import nao_nocv_2_1 as nao
import time

nao.InitProxy(IP="192.168.0.105")
nao.InitPose()
nao.Say("I am happy")

time.sleep(3)

nao.RunMovement("CheckTime.py", post = False)
nao.RunMovement("Bathroom.py", post = False)
nao.RunMovement('Nod.py', post = False)
nao.RunMovement('Right_hand.py', post = False)
nao.RunMovement('Left_hand.py', post = False)
nao.RunMovement('psv1.py', post = False)
nao.RunMovement('psv2.py', post = False)
nao.RunMovement('vangogh1.py', post = False)
nao.RunMovement('vangogh2.py', post = False)


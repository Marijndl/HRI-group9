import nao_nocv_2_1 as nao
import time

nao.InitProxy(IP="192.168.0.116")
nao.InitPose()
nao.Say("I am happy")

time.sleep(3)

nao.RunMovement("CheckTime.py", post = False)
time.sleep(1)

nao.RunMovement('vangogh1.py', post = False)
time.sleep(1)

nao.RunMovement('psv1.py', post = False)
time.sleep(1)

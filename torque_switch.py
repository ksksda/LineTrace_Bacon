import time
import rsc_u485
import sys

if __name__ == '__main__':
    servo = rsc_u485.RSC_U485('/dev/ttyUSB0',460800)
    args = sys.argv

    for id in range(1,9):
        servo.torque(id,1 if int(args[1]) else 0)
        #time.sleep(1)
        print(str(id) + " servo's torque " + "on!!" if int(args[1]) else "off!!")

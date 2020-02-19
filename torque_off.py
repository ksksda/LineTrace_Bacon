import time
import rsc_u485

if __name__ == '__main__':
    servo = rsc_u485.RSC_U485('/dev/ttyUSB0',460800)

    for id in range(1,9):
        servo.torque(id,0)
        #time.sleep(1)
        print(str(id) + " servo's torque off!")

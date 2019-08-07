import time
import rsc_u485

if __name__ == '__main__':
    servo = rsc_u485.RSC_U485('/dev/ttyUSB0',460800)


    cid=int(input('cid?'))
    servo.IDchange(int(cid))
    servo.IDchange(cid)
    time.sleep(1)
    servo.RomSave()
    time.sleep(1)
    servo.torque(cid,1)
    servo.move(cid,1000,200)
    time.sleep(2)
    servo.move(cid,-1000,200)
    time.sleep(2)
    servo.move(cid,0,200)
    time.sleep(2)

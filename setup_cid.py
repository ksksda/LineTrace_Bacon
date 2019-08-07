import time
import rsc_u485

if __name__ == '__main__':
    servo = rsc_u485.RSC_U485('/dev/ttyUSB0',460800)

    print("cid?")
    cid=input()
    servo.IDchange(int(cid))
    time.sleep(1)
    servo.RomSave()
    time.sleep(1)

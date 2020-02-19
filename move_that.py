import time
import rsc_u485

if __name__ == '__main__':
    servo = rsc_u485.RSC_U485('/dev/ttyUSB0',460800)

    while True:
    	  cid=int(input('cid?'))
        servo.torque(cid,1)
        print(str(cid) + " servo's torque on!")
        while True:
            print("angle?: ",end="")
            ang=input()
            if ang == 'q':
                break
            servo.move(cid,int(ang),100)
            time.sleep(1)

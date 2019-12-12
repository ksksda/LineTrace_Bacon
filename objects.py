import serial
import time
import rsc_u485

class robot_control(object):
    def __init__(self):
        self.gpio_seri = serial.Serial('/dev/ttyACM0',9600)
        self.servo = rsc_u485.RSC_U485('/dev/ttyUSB0',460800)
        self.motor = [0., 0.]
        self.servo = [0, 0, 0, 0, 0]
        self.gate = [0, 0, 0]
        self.sensor = [0, 0, 0, 0]
        self.dist = 0.
        self.c = 0
        for i in range(8):
            self.servo.torque(i + 1, 1)
        
    def __iter__(self):
        return self
    def __next__(self):
        snd = ''
        for f in self.motor:
            snd += str(f) + ' '
        self.gpio_seri.write(snd + 'e')
            
        for i in range(5):
            self.servo.move(i + 1, 10*self.servo[i], 1)
        for i in range(3):
            self.servo.move(i + 1, -1200*self.gate[i], 1)
        
        ret = ''
        while not ret:
            time.sleep(0.005)
            ret = self.gpio_seri.readline()
        r = ret.split(' ')
        for i in range(4):
            self.sensor[i] = int(r[i])
        self.dist = 34541.0/(float(r[4])+float(r[5])) - 6.0348

    def identify_color(self):
        self.c += 1
        return (self.c-1) // 5


import serial
import time
import rsc_u485

class robot_control(object):
    def __init__(self):
        
        for _ in range(10):
            try:
                self._arduino = serial.Serial('/dev/ttyACM0',9600)
                break
            except FileNotFoundError:
                self._arduino = None
        
        for _ in range(10):
            try:
                self._rs485 = rsc_u485.RSC_U485('/dev/ttyUSB0',460800)
                break
            except FileNotFoundError:
                self._rs485 = None
        
        self.motor = [0., 0.]
        self.servo = [0, 0, 0, 0, 0]
        self.gate = [0, 0, 0]
        self.sensor = [0, 0, 0, 0]
        self.dist = 0.
        self.c = 0
        if self._rs485:
            for i in range(8):
                self._rs485.torque(i + 1, 1)
        
    def __iter__(self):
        return self
    def __next__(self):
        
        if self._rs485:
            for i in range(5):
                self._rs485.move(i + 1, 10*self.servo[i], 1)
            for i in range(3):
                self._rs485.move(i + 1, -1200*self.gate[i], 1)
        
        if self._arduino:
            snd = ''
            for f in self.motor:
                snd += str(f) + ' '
            print("send: \"" + snd + "\"")
            self._arduino.write((snd + 'e').encode('UTF-8'))
            
            ret = self._arduino.readline().decode('UTF-8')
            print("return: \"" + ret + "\"")
            r = ret.split(' ')
            if len(r)<6:
                return
            for i in range(4):
                self.sensor[i] = int(r[i])
            self.dist = 34541.0/(float(r[4])+float(r[5])) - 6.0348

    def identify_color(self):
        self.c += 1
        return (self.c-1) // 5


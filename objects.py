import serial
import time

class robot_control(object):
	def __init__(self):
		self.gpio_seri = serial.Serial('/dev/ttyACM0',9600)
		self.motor = [0., 0.]
		self.servo = [0, 0, 0, 0, 60]
		self.gate = [0, 0, 0]
		self.sensor = [0, 0, 0]
		self.dist = 0.
		
	def __iter__(self):
		return self
	def __next__(self):
		snd = ''
		for f in self.motor:
			snd += str(f) + ' '
		for f in self.servo:
			snd += str(f) + ' '
		for f in self.gate:
			snd += str(f) + ' '
		self.gpio_seri.write(snd + 'e')
		ret = ''
		while not ret:
			time.sleep(0.005)
			ret = self.gpio_seri.readline()
		r = ret.split(' ')
		for i in range(3):
			self.sensor[i] = int(r[i])
		self.dist = float(r[3])
	
	def identify_color(self):
		clr = 0
		return clr

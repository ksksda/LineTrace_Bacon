import time
import linetrace
import objects

balls = [0, 0, 0]

def seek():
	border = 350
	flg1 = 0
	flg2 = 0
	yield None
	
	while True:
		if objects.measure_dist() < border:
			yield approach
		sensor = objects.sense_line()
		if not flg2 and (sensor[0] or sensor[3]):
			flg1 ^= 1
			objects.mc = objects.motor_control(1., 0.) if flg1 else objects.motor_control(0., 1.)
		if flg2 and not (sensor[0] or sensor[3]):
			flg2 ^= 1
		yield None

def approach():
	border = 200
	objects.mc = objects.motor_control(0.5, 0.5)
	yield None
	
	while True:
		if objects.measure_dist() < border:
			yield catch
		yield None

def capture():
	###
	key_angles = [[],[],[]]
	capture_angles = [[[],[]],[[],[]],[[],[]]]
	objects.mc = objects.motor_control(0., 0.)
	yield None
	
	clr = objects.identify_color()
	balls[clr] += 1
	key_angles.expend(capture_angles(clr))
	yield None
	
	for angles in key_angles:
		objects.servo_control(angles)
		t = time.time()
		while time.time() - t < 1.:
			yield None
	
	yield turn if sum(balls)==15 else back

def throw():
	###
	key_angles = [[],[],[]]
	objects.mc = objects.motor_control(0., 0.)
	yield None
	
	for angles in key_angles:
		objects.servo_control(angles)
		t = time.time()
		while time.time() - t < 1.:
			yield None
	yield linetrace.linetrace

def back():
	objects.mc = objects.motor_control(-0.5, -0.5)
	yield None
	
	while True:
		if any(objects.sense_line()):
			yield seek
		yield None
	
def turn():
	objects.mc = objects.motor_control(0.5, -0.5)
	yield None
	
	while True:
		if not any(objects.sense_line()):
			break
		yield None
	while True:
		if any(objects.sense_line()):
			yield linetrace.shoot
		yield None


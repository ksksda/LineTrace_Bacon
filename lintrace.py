import capture
import time

line_crossed = 0
off_flag = False

def straight(rc):		# 最初にラインを見つけるまで走る
	rc.motor = [0.5,0.5]
	yield None
	while True:
		if any(rc.sensor):
			yield linetrace
		yield None

def linetrace(rc):	# ライントレース、ラインクロス1回でcapture.throw、4回でcapture.seek
	yield None
	while True:
		if all(rc.sensor):
			if not off_flag:
				line_crossed += 1
				off_flag = True
			if line_crossed == 2:
				yield capture.throw
			elif line_crossed == 4:
				yield capture.seek
			elif line_crossed == 6:
				yield capture.shoot
			# elif line_crossed >= 7:
			# yield capture.shoot2
		else:
			off_flag = False
		
		if not off_flag:
			if rc.sensor[0]:
				rc.motor = [0.25,0.75]
			elif rc.sensor[2]
				rc.motor = [0.75,0.25]
			else:
				rc.motor = [0.5,0.5]
	yield None

def shoot(rc):		# ボールを全部拾ったあと、ボールが落ちているフィールドにおいてその場転回した後に実行される。ボールをゴールに入れる
	rc.motor = [0.5,0.5]
	yield None
	while True:
		if not all(rc.sensor):
			if off_flag:
				off_flag = False
		if all(rc.sensor) and not off_flag:
			break

	rc.motor = [0.5,-0.5]
	yield None
	while True:
		if not any(rc.sensor):
			break
		yield None
	while True:
		if rc.sensor[1]:
			break
		yield None
	rc.motor = [0,0]
	rc.gate = [1,1,1]
	yield None
	time.sleep(1.0)
	for i in range(3):
		rc.gate[1] = 0
		yield None
		time.sleep(0.5)
	# rc.motor = [0.5,-0.5]
	# yield None
	# while True:
	#	 if not any(rc.sensor):
	#		 break
	#	 yield None
	# while True:
	#	 if all(rc.sensor):
	#		 yield linetrace
	#	 yield None
	

def shoot2(rc):		# ボールを全部拾ったあと、ボールが落ちているフィールドにおいてその場転回した後に実行される。ボールをゴールに入れる
	#TODO 将来の課題
	pass

def goal(rc):			# 初期位置に戻って止まる
	pass

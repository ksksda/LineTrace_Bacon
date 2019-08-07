import time
import linetrace

balls = [0, 0, 0]

def seek(rc):
    border = 350 
        flg1 = 0
        flg2 = 0
        yield None

        while True:
            if rc.dist < border:
                yield approach
                sensor = rc.sensor
                if not flg2 and (sensor[0] or sensor[2]):
                    flg1 ^= 1
                        rc.motor = [1., 0.] if flg1 else [0., 1.]
                if flg2 and not (sensor[0] or sensor[2]):
                    flg2 ^= 1
                yield None

def approach(rc):
    border = 200
        rc.motor = [0.5, 0.5]
        yield None

        while True:
            if rc.dist < border:
                yield capture
                yield None

def capture(rc):
    key_angles = [[0,115,80,-105,0],[0,120,30,-60,0],[0,120,30,-60,60]]
        capture_angles = [[[50,35,-70,-90,60],[50,35,-70,-90,0]],[[0,35,-70,-90,60],[0,35,-70,-90,0]],[[-50,35,-70,-90,60],[-50,35,-70,-90,0]]]
        rc.motor = [0., 0.]
        yield None

        clr = rc.identify_color()
        balls[clr] += 1
        key_angles.extend(capture_angles[clr])
        yield None

        for angles in key_angles:
            rc.servo = angles
                t = time.time()
                while time.time() - t < 1.:
                    yield None

        yield back

def throw(rc):
    key_angles = [[90,0,0,0,60],[90,30,90,60,60],[90,30,90,0,0],[0,0,0,0,0]]
        rc.motor = [0., 0.]
        yield None

        for angles in key_angles:
            rc.servo = angles
                t = time.time()
                while time.time() - t < 1.:
                    yield None
        yield linetrace.linetrace

def back(rc):
    rc.motor = [-0.5, -0.5]
        yield None

        while True:
            if sum(balls)==15:
                yield turn
            elif any(rc.sensor):
                yield seek
            yield None

def turn(rc):
    rc.motor = [0.5, -0.5]
        yield None

        while True:
            if not any(rc.sensor):
                break
            yield None
        while True:
            if rc.sensor[1]:
                yield linetrace.linetrace
            yield None

import capture
import time
import sys
import DQN_ksksda

line_crossed = 0
off_flag = False


def shoot_first(rc):      # ボールを全部拾ったあと、ボールが落ちているフィールドを抜けた後に実行される。ボールをゴールに入れる
    
    rc.motor = [0.5,0.5]
    yield None
    time.sleep(1.5)
    rc.motor = [-0.5,-0.5]
    yield None
    time.sleep(1.5)
    rc.motor = [0.25,-0.25]
    yield None
    time.sleep(0.5)
    #yield DQN_ksksda.linetrace_DQN_ksksda
    yield linetrace
    
def linetrace(rc):  # ライントレース、ラインクロス1回でcapture.throw、4回でcapture.seek
    global off_flag
    global line_crossed
    yield None
    while True:
        if all(rc.sensor):
            if not off_flag:
                line_crossed += 1
                off_flag = True
        elif off_flag:
            off_flag = False
            # if line_crossed == 3:
            #     yield capture.throw
            # elif line_crossed == 5:
            #     yield capture.seek
            # elif line_crossed == 6:
            #     yield shoot
            # elif line_crossed >= 7:
            # yield shoot2
        
        rc.motor = [0.5,0.5]
        if not off_flag:
            if rc.sensor[3]:
                rc.motor[0] = 0.85
            elif not rc.sensor[2]:
                rc.motor[0] = 0.15
            if rc.sensor[0]:
                rc.motor[1] = 0.85
            elif not rc.sensor[1]:
                rc.motor[1] = 0.15
        yield None

def shoot(rc):      # ボールを全部拾ったあと、ボールが落ちているフィールドを抜けた後に実行される。ボールをゴールに入れる
    global off_flag
    global line_crossed
    
    rc.motor = [0.5,-0.5]
    yield None
    while True:
        if not all(rc.sensor):
            off_flag = False
        if rc.sensor[0] and not rc.sensor[1]:
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
    
    # demo
    '''
    for i in range(3):
        rc.gate[i] = 0
        yield None
        time.sleep(0.5)
    while True:
        yield None
    '''
    
    # gachi
    rc.motor = [0.5,0.5]
    rc.gate = [0,0,0]
    yield None
    time.sleep(1.0)
    yield capture.turn

def shoot2(rc):     # ボールを全部拾ったあと、ボールが落ちているフィールドにおいてその場転回した後に実行される。ボールをゴールに入れる
    #TODO 将来の課題
    pass

def goal(rc):       # 初期位置に戻って止まる
    pass


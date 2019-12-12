import capture
import time

line_crossed = 0
off_flag = False

def straight(rc):   # 最初にラインを見つけるまで走る
    rc.motor = [0.5,0.5]
    yield None
    #sleep(1)
    while True:
        if any(rc.sensor):
            yield linetrace
        yield None

def linetrace(rc):  # ライントレース、ラインクロス1回でcapture.throw、4回でcapture.seek
    yield None
    while True:
        if all(rc.sensor):
            if not off_flag:
                line_crossed += 1
                off_flag = True
        else:
            off_flag = False
            if line_crossed == 2:
                yield capture.throw
            elif line_crossed == 4:
                yield capture.seek
            elif line_crossed == 6:
                yield capture.shoot
            # elif line_crossed >= 7:
            # yield capture.shoot2
        
        if off_flag:
            rc.motor = [0.5,0.5]
        else:
            if rc.sensor[0]:
                rc.motor = [0.25,0.75]
            elif rc.sensor[2]
                rc.motor = [0.75,0.25]
            else:
                rc.motor = [0.5,0.5]
    yield None

def shoot(rc):      # ボールを全部拾ったあと、ボールが落ちているフィールドにおいてその場転回した後に実行される。ボールをゴールに入れる
    rc.motor = [0.5,0.5]
    yield None
    while True:
        if all(rc.sensor):
            if not off_flag:
                line_crossed += 1
                off_flag = True
                break
        yield None
    
    rc.motor = [0.5,-0.5]
    yield None
    while True:
        if not any(rc.sensor):
            off_flag = False
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
    yield linetrace

def shoot2(rc):     # ボールを全部拾ったあと、ボールが落ちているフィールドにおいてその場転回した後に実行される。ボールをゴールに入れる
    #TODO 将来の課題
    pass

def goal(rc):       # 初期位置に戻って止まる
    pass


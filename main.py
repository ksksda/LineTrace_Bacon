import linetrace
import capture
import objects
import time

rc = objects.robot_control()
loop_func = linetrace.shoot_first
func_name = ""

if __name__ == '__main__':
    time.sleep(3)
    while True:
        if loop_func:
            lf = loop_func(rc)
            next(lf)
            func_name = loop_func.__name__
            loop_func = None
        loop_func = lf.send(next(rc))
        print(func_name)

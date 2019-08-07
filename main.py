import linetrace
import capture
import objects

rc = objects.robot_control()
loop_func = linetrace.straight

if __name__ == '__main__':
	while True:
		if loop_func:
			lf = loop_func(rc)
			next(lf)
			loop_func = None
		loop_func = lf.send(next(rc))

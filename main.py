import linetrace
import capture
import objects

loop_func = linetrace.straight

if __name__ == '__main__':
	while True:
		if loop_func:
			lf = loop_func()
			next(lf)
			loop_func = None
		loop_func = lf.send(next(objects.mc))


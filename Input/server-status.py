import commands

def main(inputs):
	for inp in inputs:
		(cS, c0) = commands.getstatusoutput('ping -c1 %s' % inp)
		while True:
			if 0 != cS:
				# Server down.
				Notify.Send('Server %s is down' % inp)
				break
			else:
				break

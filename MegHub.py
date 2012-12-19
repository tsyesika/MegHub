import Core.Notify as notify
import sys, glob, imp, os, time

if __name__ == "__main__":
	try:
		import config
	except:
		print "There seems to be a problem with your config."
		raise
		sys.exit()

	# Create a notifier.
	input_notifiers = {}
	inputs = {}
	for inp in glob.glob("Input/*.py"): 
		if inp in config.input_filters and config.input_filters[inp]:
			name = os.path.splitext(os.path.basename(inp))[0] 
			inputs[name] = imp.load_source(name, inp)
			Notify = notify.Notify(name)
			inputs[name].Notify = Notify
	while True:
		try:
			time.sleep(5)
			# at the moment do each filter 5 every 5 seconds
			for f in inputs:
				inputs[f].main(inp["inputs"])
		except KeyboardInterrupt:
			print "bye!"
			sys.exit()
		except:
			raise

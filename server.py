import socket, imp, os, glob

class Hooker():
	def __init__(self):
		self.hooks = {}
	def register_hook(self, hook, func):
		if not hook in self.hooks.keys():
			self.hooks[hook] = Set()
		self.hooks[hook].add(func)
	def unregister_hook(self, hook, func):
		if hook in self.hooks.keys() and func in self.hooks[hook]:
			self.hooks.remove(func)
	def hook(self, hook):
		if hook in self.hooks.keys():
			for hook in self.hooks[hook]:
				hook()

class Plugin():
	def __init__(self, name, location):
		self.name = name
		self.location = location
		self.instance = imp.load_source(name, location)
		
	def request(self, token, data*):
		return self.instance.request(token, data)

if __name__ == "__main__":
	plugins = {}
	for plugin in glob.glob(config.dirs["Plugins"]):
		name = os.path.splitext(os.path.basename(plugin))[0]
		plugins[name] = Plugin(name, plugin)
		if config.debug:
			print "[Plugin] added %s (%s) " % (name, plugin)
	print "Plugins Loaded"

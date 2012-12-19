import hashlib, time

class Notification():
	def __init__(self, message, action):
		self.message = message
		self.action = action
		self.hash = hashlib.sha256(self.messsage + self.action)
		self.time = time.time()

class Notify():
	def __init__(self, name):
		self.name = name
	def Send(self, message, action=None):
		# Produce a notification instance.
		self.notification = Notification(message, action)
		return self.notificaton

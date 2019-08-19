from channels.generic.websocket import WebsocketConsumer
import RPi.GPIO as GPIO

def switchon():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(23,GPIO.OUT)
	GPIO.output(23,True)
	print("light on")

def switchoff():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(23,GPIO.OUT)
	GPIO.output(23,False)
	GPIO.cleanup()
	print("light off")

class lightconsumer(WebsocketConsumer):
	flag=0
	def connect(self):
		self.accept()
		print("socket connected")

	def disconnect(self,close_code):
		print("socket disconnected")

	def receive(self,text_data):
		print("message received: ",text_data)
		if text_data=="ON":
			if self.flag==0:
				switchon()
				self.flag=1
			else:
				pass
		if text_data=="OFF":
			if self.flag==1:
				switchoff()
				self.flag=0
			else:
				pass

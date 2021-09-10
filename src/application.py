import wx
import logging
import os
import sys
from gui import main
from accessible_output2 import outputs

def setup_logging(level=logging.INFO):
	root = logging.getLogger()
	root.setLevel(level)
	formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
	ch = logging.StreamHandler(sys.stdout)
	ch.setLevel(logging.DEBUG)
	ch.setFormatter(formatter)
	root.addHandler(ch)

class Application:
	def __init__(self):
		self.name = "copy_symbol"
		self.version = 0.1
		self.running = False
		self.logger = logging
		self.speech = None
		self.wx = wx.App()
		self.main_dialog = main.MainDialog(self, f"{self.name} V{self.version}")
		self.setup_speech()

	def run(self):
		self.running = True
		self.main_dialog.Show()
		self.wx.MainLoop()

	def setup_speech(self):
		try:
			self.speech = outputs.auto.Auto()
			return True
		except:
			return False

	def say(self, text, interrupt=False):
		self.speech.speak(text, interrupt)
		self.speech.braille(text)

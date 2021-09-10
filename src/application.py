import wx
import logging
import os
import sys
from gui import main

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
		self.wx = wx.App()
		self.main_dialog = main.MainDialog(f"{self.name} V{self.version}")

	def run(self):
		self.running = True
		self.main_dialog.Show()
		self.wx.MainLoop()

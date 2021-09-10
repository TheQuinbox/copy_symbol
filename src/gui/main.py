import wx
import sys

class MainDialog(wx.Dialog):
	def __init__(self, title):
		self.title = title
		wx.Dialog.__init__(self, None, title=self.title, size=wx.DefaultSize)
		self.Bind(wx.EVT_CLOSE, self.on_close)
		self.panel = wx.Panel(self)
		self.main_box = wx.BoxSizer(wx.VERTICAL)

	def on_close(self, event=None):
		self.Destroy()
		sys.exit()

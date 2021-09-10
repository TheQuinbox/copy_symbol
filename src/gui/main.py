import wx
import sys
import symbol_list

class MainDialog(wx.Dialog):
	def __init__(self, title):
		self.title = title
		wx.Dialog.__init__(self, None, title=self.title, size=wx.DefaultSize)
		self.Bind(wx.EVT_CLOSE, self.on_close)
		self.panel = wx.Panel(self)
		self.main_box = wx.BoxSizer(wx.VERTICAL)
		self.symbols_list_label = wx.StaticText(self.panel, -1, label="Available symbols")
		self.main_box.Add(self.symbols_list_label, 0, wx.EXPAND | wx.ALL, 5)
		self.symbols_list = wx.ComboBox(self.panel, choices=list(symbol_list.SYMBOLS.keys()), style=wx.CB_SORT | wx.CB_READONLY)
		self.symbols_list.SetSelection(0)
		self.symbols_list.SetFocus()
		self.main_box.Add(self.symbols_list)
		self.panel.Layout()

	def on_close(self, event=None):
		self.Destroy()
		sys.exit()

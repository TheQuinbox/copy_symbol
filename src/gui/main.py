import wx
import sys
import symbol_list
import pyperclip

class MainDialog(wx.Dialog):
	def __init__(self, app, title):
		self.app = app
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
		self.main_box.Add(self.symbols_list, 0, wx.ALL, 10)
		self.ok_button = wx.Button(self.panel, -1, "&OK")
		self.ok_button.Bind(wx.EVT_BUTTON, self.on_ok)
		self.main_box.Add(self.ok_button, 0, wx.ALL, 10)
		self.panel.Layout()

	def on_close(self, event=None):
		self.Destroy()
		sys.exit()

	def on_ok(self, event=None):
		selected_symbol = symbol_list.SYMBOLS[self.symbols_list.GetString(self.symbols_list.GetSelection())]
		try:
			pyperclip.copy(selected_symbol)
			self.app.logger.info(f"Coppied symbol: {selected_symbol}")
			self.app.say("Coppied.")
		except Exception as e:
			self.app.say(f"Error copying symbol. {e}")
			self.logger.info(f"Error copying symbol. {e}")

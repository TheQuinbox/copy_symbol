import wx
import sys
import symbol_list
import pyperclip
from keyboard_handler.wx_handler import WXKeyboardHandler

class MainDialog(wx.Dialog):
	def __init__(self, app, title):
		self.app = app
		self.title = title
		self.hidden = False
		self.handler = WXKeyboardHandler(self)
		key = self.handler.register_key("control+win+shift+s", self.on_hide)
		wx.Dialog.__init__(self, None, title=self.title, size=wx.DefaultSize)
		self.Bind(wx.EVT_CLOSE, self.on_hide)
		self.panel = wx.Panel(self)
		self.main_box = wx.BoxSizer(wx.VERTICAL)
		self.symbols_list_label = wx.StaticText(self.panel, -1, label="Available symbols")
		self.main_box.Add(self.symbols_list_label, 0, wx.EXPAND | wx.ALL, 5)
		self.symbols_list = wx.ComboBox(self.panel, choices=list(symbol_list.SYMBOLS.keys()), style=wx.CB_SORT | wx.CB_READONLY)
		self.symbols_list.SetSelection(0)
		self.symbols_list.SetFocus()
		self.main_box.Add(self.symbols_list, 0, wx.ALL, 10)
		self.copy_button = wx.Button(self.panel, -1, "&Copy")
		self.copy_button.Bind(wx.EVT_BUTTON, self.on_copy)
		self.copy_button.SetDefault()
		self.main_box.Add(self.copy_button, 0, wx.ALL, 10)
		self.close_button = wx.Button(self.panel, -1, "E&xit")
		self.close_button.Bind(wx.EVT_BUTTON, self.on_close)
		self.main_box.Add(self.close_button, 0, wx.ALL, 10)
		self.panel.Layout()

	def on_close(self, event=None):
		self.Destroy()
		sys.exit()

	def on_copy(self, event=None):
		selected_symbol = symbol_list.SYMBOLS[self.symbols_list.GetString(self.symbols_list.GetSelection())]
		try:
			pyperclip.copy(selected_symbol)
			self.app.logger.info(f"Coppied symbol: {selected_symbol}")
			self.app.say("Coppied.")
		except Exception as e:
			self.app.say(f"Error copying symbol. {e}")
			self.logger.info(f"Error copying symbol. {e}")

	def on_hide(self, event=None):
		if self.hidden:
			self.hidden = False
			self.Show()
			self.app.logger.info("Window shown.")
		else:
			self.hidden = True
			self.Hide()
			self.app.logger.info("Window hidden.")

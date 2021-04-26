# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
import time
import wx
import wx.xrc
import wx.grid
import os
###########################################################################
## Class MyFrame15
###########################################################################
def fetch_data_true(directory):
	data = []
	full_directory = os.getcwd() if directory == '' else directory
	files = os.listdir(full_directory)

	for i in files:
		if i[i.rfind('.'):] != '.py':
			continue

		start_time = time.time()
		result = os.startfile(full_directory + "/" + i)
		end_time = time.time()
		seconds = (end_time - start_time) / 1000
		if seconds < 5:
			time_check = True
		result_check = True
		if time_check and result_check:
			data.append([i, str(seconds), 'zaliczone'])
		else:
			data.append([i, str(seconds), 'niezaliczone'])

	return data


def mock_fetch_data(directory):
	dane = []
	if directory == '':
		pliki = os.listdir()
	else:
		pliki = os.listdir(directory)
	for i in range(len(pliki)):
		dane.append([pliki[i], str(i), 'zaliczone'])

	#przykladowe_dane = [['plik1.c', "13", 'zaliczone'], ['plik2.c', "23", 'zaliczone'], ['plik3.c', "33", 'zaliczone']]
	return dane


def fetch_data(directory):
	#dane = mock_fetch_data(directory)
	dane = fetch_data_true(directory)
	return dane

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 704,565 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 600,300 ), wx.DefaultSize )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"SPRAWDZARKA PROGRAMOW - PYTHON", wx.DefaultPosition, wx.Size( -1,25 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer34.Add( self.m_staticText32, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer33.Add( bSizer34, 2, wx.EXPAND, 5 )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Wybieranie folderu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer35.Add( self.m_staticText33, 0, wx.ALL, 5 )

		self.m_dirPicker4 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer35.Add( self.m_dirPicker4, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Sprawdz", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetMaxSize( wx.Size( 200,-1 ) )

		bSizer35.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer33.Add( bSizer35, 4, wx.EXPAND, 5 )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Wyniki", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Arial Narrow" ) )

		bSizer36.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )

		# Grid
		self.m_grid1.CreateGrid( 0, 3 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.SetColSize( 0, 238 )
		self.m_grid1.SetColSize( 1, 145 )
		self.m_grid1.SetColSize( 2, 332 )
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_grid1.SetMinSize( wx.Size( -1,200 ) )

		bSizer36.Add( self.m_grid1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer33.Add( bSizer36, 10, wx.EXPAND, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Zakoncz", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.SetMaxSize( wx.Size( 200,-1 ) )

		bSizer33.Add( self.m_button3, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer33 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_LEFT_UP, self.m_button1OnLeftUp )
		self.m_button3.Bind( wx.EVT_LEFT_UP, self.m_button3OnLeftUp )

		self.m_grid1.SetColLabelValue(0, "Nazwa programu")
		self.m_grid1.SetColLabelValue(1, "Czas w sekundach")
		self.m_grid1.SetColLabelValue(2, "Poprawnosc")




	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def m_button1OnLeftUp( self, event ):
		numrows = self.m_grid1.NumberRows
		data = fetch_data( self.m_dirPicker4.GetPath())
		self.m_staticText3.SetLabel("Wyniki: znaleziono " + str(len(data)) + " plikow")
		if numrows != 0:
			self.m_grid1.DeleteRows(0, numrows)
		if not data:
			event.Skip()
		self.m_grid1.InsertRows(0, len(data))

		for i in range(len(data)):
			for j in range(self.m_grid1.NumberCols):
				self.m_grid1.SetCellValue(i, j, data[i][j])

		event.Skip()

	def m_button3OnLeftUp( self, event ):
		self.Close()
		event.Skip()



class W5(wx.App):
	def OnInit(self):
		mainFrame = MyFrame1(None)
		mainFrame.Show(True)
		return True

W5().MainLoop()

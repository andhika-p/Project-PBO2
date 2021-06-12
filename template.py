# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class Frame_Login
###########################################################################

class Frame_Login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,500 ), 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.username_login_input = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.username_login_input, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		fgSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.password_login_input = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer3.Add( self.password_login_input, 0, wx.ALL, 5 )


		fgSizer2.Add( fgSizer3, 1, wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel1.SetSizer( fgSizer2 )
		self.m_panel1.Layout()
		fgSizer2.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"Login", False )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer4 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText5 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		fgSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.username_registrasi_input = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.username_registrasi_input, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		fgSizer5.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.password_registrasi_input = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer5.Add( self.password_registrasi_input, 0, wx.ALL, 5 )


		fgSizer4.Add( fgSizer5, 1, wx.EXPAND, 5 )

		self.m_button2 = wx.Button( self.m_panel2, wx.ID_ANY, u"Registrasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_button2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel2.SetSizer( fgSizer4 )
		self.m_panel2.Layout()
		fgSizer4.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"Registrasi", True )

		fgSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.function_Login )
		self.m_button2.Bind( wx.EVT_BUTTON, self.function_registrasi )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def function_Login( self, event ):
		event.Skip()

	def function_registrasi( self, event ):
		event.Skip()


###########################################################################
## Class Frame_Aplikasi
###########################################################################

class Frame_Aplikasi ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_notebook3 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,500 ), 0 )
		self.panel_tambah_komsumsi = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer8 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText7 = wx.StaticText( self.panel_tambah_komsumsi, wx.ID_ANY, u"Jumlah Kalori", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		fgSizer8.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.jumlah_kalori_input = wx.TextCtrl( self.panel_tambah_komsumsi, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.jumlah_kalori_input, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self.panel_tambah_komsumsi, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self.panel_tambah_komsumsi, wx.ID_ANY, u"Jumlah Protein", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		fgSizer8.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.jumlah_protein_input = wx.TextCtrl( self.panel_tambah_komsumsi, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.jumlah_protein_input, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self.panel_tambah_komsumsi, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_button4, 0, wx.ALL, 5 )


		self.panel_tambah_komsumsi.SetSizer( fgSizer8 )
		self.panel_tambah_komsumsi.Layout()
		fgSizer8.Fit( self.panel_tambah_komsumsi )
		self.m_notebook3.AddPage( self.panel_tambah_komsumsi, u"Tambah Asupan", False )
		self.panel_riwayat = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.tabel_riwayat = wx.grid.Grid( self.panel_riwayat, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabel_riwayat.CreateGrid( 0, 1 )
		self.tabel_riwayat.EnableEditing( True )
		self.tabel_riwayat.EnableGridLines( True )
		self.tabel_riwayat.EnableDragGridSize( False )
		self.tabel_riwayat.SetMargins( 0, 0 )

		# Columns
		self.tabel_riwayat.SetColSize( 0, 200 )
		self.tabel_riwayat.EnableDragColMove( False )
		self.tabel_riwayat.EnableDragColSize( True )
		self.tabel_riwayat.SetColLabelSize( 30 )
		self.tabel_riwayat.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel_riwayat.EnableDragRowSize( True )
		self.tabel_riwayat.SetRowLabelSize( 80 )
		self.tabel_riwayat.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabel_riwayat.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer9.Add( self.tabel_riwayat, 0, wx.ALL, 5 )


		self.panel_riwayat.SetSizer( fgSizer9 )
		self.panel_riwayat.Layout()
		fgSizer9.Fit( self.panel_riwayat )
		self.m_notebook3.AddPage( self.panel_riwayat, u"Riwayat", True )

		fgSizer6.Add( self.m_notebook3, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( fgSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button3.Bind( wx.EVT_BUTTON, self.function_tambah_kalori )
		self.m_button4.Bind( wx.EVT_BUTTON, self.function_tambah_protein )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def function_tambah_kalori( self, event ):
		event.Skip()

	def function_tambah_protein( self, event ):
		event.Skip()



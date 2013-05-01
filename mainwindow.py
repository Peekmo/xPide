###########################################################
#### MainWindow.py
#### Created : 04-29-2013
#### Last Update : 04-30-2013
#### By Peekmo
###########################################################

#! /usr/bin/python
#-*-coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import os
import sys

from onglet import *

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		QFontDatabase.addApplicationFont("fonts/Inconsolata.otf")

		self.onglets = []

		self.initialiserFenetre()
		self.initialiserMenuFichier()
		self.initialiserMenuEdition()
		self.initialiserMenuAffichage()

		self.dock = QDockWidget("Fichiers", self)
		self.dock.setMinimumWidth(150)
		self.tree = QTreeView()
		self.dock.setWidget(self.tree)
		self.addDockWidget(Qt.LeftDockWidgetArea, self.dock)

		self.tabWidget = QTabWidget()
		self.tabWidget.setMovable(True)
		self.tabWidget.setUsesScrollButtons(True)
		self.setCentralWidget(self.tabWidget)

		self.connect(self.actionNew, SIGNAL("triggered()"), self.newFile)

		self.newFile()

	def newFile(self):
		self.newOnglet()
		self.tabWidget.addTab(self.onglets[-1], "Nouveau")

	def newOnglet(self):
		onglet = Onglet(self)
		self.onglets.append(onglet)

	def initialiserFenetre(self):
		self.setWindowTitle("IDE")
		self.setMinimumSize(700, 500)

	def initialiserMenuFichier(self):
		self.menuFichier = self.menuBar().addMenu("Fichier")

		# Actions
		self.actionNew = self.menuFichier.addAction("Nouveau")
		self.actionOpen = self.menuFichier.addAction("Ouvrir")
		self.actionClose = self.menuFichier.addAction("Fermer")

		self.menuFichier.addSeparator()

		self.actionSave = self.menuFichier.addAction("Enregistrer")
		self.actionSaveAs = self.menuFichier.addAction("Enregistrer sous...")

		self.menuFichier.addSeparator()

		self.actionExit = self.menuFichier.addAction("Quitter")

		# Raccourcis
		self.actionNew.setShortcut(QKeySequence("Ctrl+N"))
		self.actionOpen.setShortcut(QKeySequence("Ctrl+O"))
		self.actionClose.setShortcut(QKeySequence("Ctrl+F"))
		self.actionSave.setShortcut(QKeySequence("Ctrl+S"))
		self.actionSaveAs.setShortcut(QKeySequence("Ctrl+Shift+S"))
		self.actionExit.setShortcut(QKeySequence("Ctrl+Q"))

	def initialiserMenuEdition(self):
		self.menuEdition = self.menuBar().addMenu(self.trUtf8("Edition"))

		# Actions
		self.actionUndo = self.menuEdition.addAction("Annuler")
		self.actionRedo = self.menuEdition.addAction(self.trUtf8("Retablir"))

		self.menuEdition.addSeparator()

		self.actionCut = self.menuEdition.addAction("Couper")
		self.actionCopy = self.menuEdition.addAction("Copier")
		self.actionPaste = self.menuEdition.addAction("Coller")

		self.menuEdition.addSeparator()

		self.actionSelectAll = self.menuEdition.addAction(self.trUtf8("Tout selectionner"))

		# Raccourcis
		self.actionUndo.setShortcut(QKeySequence("Ctrl+Z"))
		self.actionRedo.setShortcut(QKeySequence("Ctrl+Y"))
		self.actionCut.setShortcut(QKeySequence("Ctrl+X"))
		self.actionCopy.setShortcut(QKeySequence("Ctrl+C"))
		self.actionPaste.setShortcut(QKeySequence("Ctrl+V"))
		self.actionSelectAll.setShortcut(QKeySequence("Ctrl+A"))

	def initialiserMenuAffichage(self):
		self.menuAffichage = self.menuBar().addMenu("Affichage")


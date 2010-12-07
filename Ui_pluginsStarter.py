# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_pluginsStarter.ui'
#
# Created: Tue Dec  7 10:00:06 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_pluginsStarterGuibase(object):
    def setupUi(self, pluginsStarterGuibase):
        pluginsStarterGuibase.setObjectName("pluginsStarterGuibase")
        pluginsStarterGuibase.resize(326, 280)
        self.gridLayout = QtGui.QGridLayout(pluginsStarterGuibase)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title = QtGui.QLabel(pluginsStarterGuibase)
        self.title.setObjectName("title")
        self.verticalLayout_2.addWidget(self.title)
        self.scrollArea = QtGui.QScrollArea(pluginsStarterGuibase)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 304, 202))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.buttonBox = QtGui.QDialogButtonBox(pluginsStarterGuibase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(pluginsStarterGuibase)
        QtCore.QMetaObject.connectSlotsByName(pluginsStarterGuibase)

    def retranslateUi(self, pluginsStarterGuibase):
        pluginsStarterGuibase.setWindowTitle(QtGui.QApplication.translate("pluginsStarterGuibase", "Plugin starter settings", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setText(QtGui.QApplication.translate("pluginsStarterGuibase", "Enable Actions", None, QtGui.QApplication.UnicodeUTF8))


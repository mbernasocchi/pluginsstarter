# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_pluginsStarter.ui'
#
# Created: Mon Dec  6 18:26:28 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_pluginsStarterGuibase(object):
    def setupUi(self, pluginsStarterGuibase):
        pluginsStarterGuibase.setObjectName("pluginsStarterGuibase")
        pluginsStarterGuibase.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(pluginsStarterGuibase)
        self.buttonBox.setGeometry(QtCore.QRect(50, 260, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.title = QtGui.QLabel(pluginsStarterGuibase)
        self.title.setGeometry(QtCore.QRect(10, 10, 99, 17))
        self.title.setObjectName("title")
        self.scrollArea = QtGui.QScrollArea(pluginsStarterGuibase)
        self.scrollArea.setGeometry(QtCore.QRect(10, 30, 381, 221))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 379, 219))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(pluginsStarterGuibase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), pluginsStarterGuibase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), pluginsStarterGuibase.reject)
        QtCore.QMetaObject.connectSlotsByName(pluginsStarterGuibase)

    def retranslateUi(self, pluginsStarterGuibase):
        pluginsStarterGuibase.setWindowTitle(QtGui.QApplication.translate("pluginsStarterGuibase", "Plugin starter settings", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setText(QtGui.QApplication.translate("pluginsStarterGuibase", "Enable Actions", None, QtGui.QApplication.UnicodeUTF8))


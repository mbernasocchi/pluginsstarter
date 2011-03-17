"""
/***************************************************************************
pluginsStarterDialog
A QGIS plugin
test pluginsStarter plugin description
                             -------------------
begin                : 2010-08-18 
copyright            : (C) 2010 by Marco Bernasocchi BERNAWEBDESIGN.CH
email                : marco@bernawebdesign.ch 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
#FIXME: fix icons 
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from Ui_pluginsStarter import Ui_pluginsStarterGuibase

# create the dialog
class pluginsStarterDialog(QDialog):
  def __init__(self, main):
    QDialog.__init__(self)
    # Set up the user interface from Designer. 
    self.ui = Ui_pluginsStarterGuibase()
    self.ui.setupUi(self)
    self.main = main
    self.settings = QSettings()
    
    #get all actions from the plugin toolbar
    availableActions = self.main.iface.pluginToolBar().actions()
    #availableActions = self.main.iface.pluginMenu().actions() #can also be used
    
    actionsBlackList = [self.main.runActionName, self.main.settingsActionName]
        
    #create the checkboxes and connect them to the actions
    self.checkboxes = []
    for action in availableActions:
      if action.text() not in actionsBlackList:
        c = QCheckBox(action.text())
        isOn = self.settings.value('/PluginsStarter/' + action.text() , QVariant( False ) ).toBool()
        c.setChecked(isOn)
        self.ui.verticalLayout.addWidget(c)
        self.checkboxes.append({'box':c, 'action':action})
      
  def updateSettings( self ):
    self.main.runActions = []
    for checkbox in self.checkboxes:
      if checkbox['box'].isChecked():
        self.settings.setValue( '/PluginsStarter/' + checkbox['box'].text(), QVariant( True ) )
        self.main.runActions.append( checkbox['action'] )
      else:
        self.settings.setValue( '/PluginsStarter/' + checkbox['box'].text(), QVariant( False ) )
    
  @pyqtSlot()
  def on_buttonBox_accepted(self):
    self.updateSettings()

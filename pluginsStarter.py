"""
/***************************************************************************
pluginsStarter
A QGIS plugin
Start multiple plugins in one click
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import resources_rc
# Initialize Qt resources from file resources_rc.py
# import resources is done in Ui_pluginsStarter
# Import the code for the dialog
from pluginsStarterDialog import pluginsStarterDialog

class pluginsStarter:

  def __init__(self, iface):
    # Save reference to the QGIS interface
    self.iface = iface
    self.map = iface.mapCanvas()
    #actions to run
    self.runActions = []
    #strings
    self.runActionName = "Start multiple plugins"
    self.settingsActionName = "Configure plugins starter"
    self.runActionText = "Start multiple plugins in one click"
    self.settingsActionText = "Configure which plugins to start with plugins starter"
    
  def initGui(self):
    #RUN ACTION
    # Create action that will start plugin
    self.runAction = QAction(QIcon(":/plugins/pluginsStarter/icon.png"), \
      self.runActionName , self.iface.mainWindow())
    # connect the action to the run method
    QObject.connect(self.runAction, SIGNAL("triggered()"), self.run)
    
    # Add toolbar button and menu item
    self.iface.addToolBarIcon(self.runAction)
    self.iface.addPluginToMenu("&Plugins Starter", self.runAction)
    self.runAction.setWhatsThis(self.runActionText)
    self.runAction.setStatusTip(self.runActionText)
    
    #SETTINGS ACTION
    # Create action that will start plugin configuration
    self.settingsAction = QAction(QIcon(":/plugins/pluginsStarter/icon.png"), \
        self.settingsActionName, self.iface.mainWindow())
    # connect the action to the settings method
    QObject.connect(self.settingsAction, SIGNAL("triggered()"), self.configure)    
    
    # Add toolbar button and menu item
    #self.iface.addToolBarIcon(self.settingsAction)
    self.iface.addPluginToMenu("&Plugins Starter", self.settingsAction)
    self.settingsAction.setWhatsThis(self.settingsActionText)
    self.settingsAction.setStatusTip(self.settingsActionText)

  def unload(self):
    # Remove the plugin menu item and icon
    self.iface.removePluginMenu("&Plugins Starter", self.runAction)
    self.iface.removePluginMenu("&Plugins Starter", self.settingsAction)
    self.iface.removeToolBarIcon(self.runAction)
    #self.iface.removeToolBarIcon(self.settingsAction)

  # run method that performs all the real work
  def run(self):
    #try to read settings (during __init__ there are no actions available yet)
    if 0 == len(self.runActions):
      pluginsStarterDialog(self).updateSettings()  
    if 0 < len(self.runActions):
      for action in self.runActions:
        action.activate(action.Trigger)
    else:
      QMessageBox.information(None, "Plugins starter", \
        "No plugins selected, please configure the plugin")
      self.configure()

  # create configuration dialog every time config is called
  # this makes the dialog always show the actual actions list
  def configure(self):
    #create configuration dialog
    settingsDialog = pluginsStarterDialog(self)
    if ( settingsDialog.exec_() ):
      pass
      

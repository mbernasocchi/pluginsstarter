#!python
"""
/***************************************************************************
pluginsStarter
A QGIS plugin
Start multiple plugins in one click
                             -------------------
begin                : 2010-11-28 
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
 This script initializes the plugin, making it known to QGIS.
"""
def authorName():
 return "Marco Bernasocchi BERNAWEBDESIGN.CH"
def name():
  return "Plugins Starter plugin"
def description():
  return "Start multiple plugins in one click"
def version():
  return "Version 1.0"
def qgisMinimumVersion():
  return "1.6"
def classFactory(iface):
  # load pluginsStarter class from file pluginsStarter
  from pluginsStarter import pluginsStarter
  return pluginsStarter(iface)


# Makefile for geoTOP PyQGIS plugin
DEPLOY_DIR = /home/marco/.qgis/python/plugins/pluginsStarter

UI_FILES = Ui_pluginsStarter.py

RESOURCE_FILES = resources.py

default: compile

compile: $(UI_FILES) $(RESOURCE_FILES)
%.py : %.qrc
  #changes the file name from resources to resources_rc 
  #to be consistent with the files generated by qt_designer
	pyrcc4 -o $*_rc.py  $<

%.py : %.ui
	pyuic4 -o $@ $<

#deploy:
#	cp -Rf *.pyc $(DEPLOY_DIR)

clean:
	$(RM) *.pyc

## Digikam-Control
This skill enables an user to control the [DigiKam client](https://www.digikam.org/) on the Desktop.

## Description 
#### Installation of skill:
* Download or Clone Git (run: git clone https://github.com/AIIX/DigiKam-control inside /opt/mycroft/skills)
* Create /opt/mycroft/skills folder if it does not exist
* Extract Downloaded Skill into a folder. "DigiKam-control". (Clone does not require this step)
* Copy the DigiKam-control folder to /opt/mycroft/skills/ folder

#### Installation of requirements:
##### Fedora: 
- sudo dnf install dbus-python
- From terminal: cp -R /usr/lib64/python2.7/site-packages/dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/
- From terminal: cp /usr/lib64/python2.7/site-packages/_dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/

##### Ubuntu / KDE Neon: 
- sudo apt install python-dbus
- From terminal: cp -R /usr/lib/python2.7/dist-packages/dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/
- From terminal: cp /usr/lib/python2.7/dist-packages/_dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/

* For other distributions:
- Python Dbus package is required and copying the Python Dbus folder and lib from your system python install over to /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/.

## Examples
##### Some of the actions, for more actions refer to "actions.json" file: 

###### Next Image
* "Hey Mycroft, in digicam next image"

###### Previous Image
* "Hey Mycroft, in digicam previous image"

###### Rotate Image Clockwise
* "Hey Mycroft, in digicam rotate clockwise"

###### Rotate Image Counter Clockwise
* "Hey Mycroft, in digicam rotate counter clockwise"

###### Flip-Horizontally
* "Hey Mycroft, in digicam flip horizontally"

###### Flip-vertically
* "Hey Mycroft, in digicam flip vertically"


## Credits 
(AIX) Aditya Mehra

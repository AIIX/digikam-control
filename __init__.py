import re
import json
import dbus
from adapt.intent import IntentBuilder
from os.path import join, dirname
from string import Template
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.skills.context import *
from mycroft.util import read_stripped_lines
from mycroft.util.log import getLogger
from mycroft.messagebus.message import Message

__author__ = 'aix'

LOGGER = getLogger(__name__)

class DigiKamControlSkill(MycroftSkill):
    def __init__(self):
        super(DigiKamControlSkill, self).__init__(name="DigiKamControlSkill")
        self.actions_index = dirname(__file__) + '/actions.json'
        
    @intent_handler(IntentBuilder("DigiKamControl").require("DigiCamKeyword").build())
    def handle_digikam_control_intent(self, message):
        utterance = message.data.get('utterance').lower()
        utterance = utterance.replace(message.data.get('DigiCamKeyword'), '')
        searchString = utterance.encode('utf-8')
        getAction = self.filterAction(searchString.lstrip())
       
        session_bus = dbus.SessionBus()
        digicam_bus = ""
        for method in session_bus.list_names():
            if method.find("digikam") != -1:
                digicam_bus = method
                break

        digicamObj = session_bus.get_object(digicam_bus, "/Digikam")
        digicamObj.activateAction(getAction, dbus_interface = "org.kde.KMainWindow")
       
    def filterAction(self, event):
        action = event.lower()
        with open(self.actions_index) as json_data:
            d = json.load(json_data)
            if action in d["next_image"]:
                return "next_image"
            elif action in d["previous_image"]:
                return "previous_image"
            elif action in d["first_image"]:
                return "first_image"
            elif action in d["last_image"]:
                return "last_image"
            elif action in d["view_refresh"]:
                return "view_refresh"
            elif action in d["browse_album"]:
                return "browse_album"
            elif action in d["rotate_ccw"]:
                return "rotate_ccw"
            elif action in d["rotate_cw"]:
                return "rotate_cw"
            elif action in d["flip_horizontal"]:
                return "flip_horizontal"
            elif action in d["flip_vertical"]:
                return "flip_vertical"
            elif action in d["selectAll"]:
                return "selectAll"
            elif action in d["selectInvert"]:
                return "selectInvert"
            else:
                self.speak("Action Not Found");
        
    def stop(self):
        pass
    
def create_skill():
    return DigiKamControlSkill()

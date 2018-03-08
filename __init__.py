
from adapt.intent import IntentBuilder
from mycroft.skills.score import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'mathias'

LOGGER = getLogger(__name__)

class HerokuStatusSkill(MycroftSkill):
    def __init__(self):
        super(HerokuStatusSkill, self).__init__(name="HerokuStatusSkill")

    def initialize(self):
        intent = IntentBuilder("HerokuStatusIntent").require("HerokuStatusKeyword").build()
        self.register_intent(intent, self.handle_intent)

    def handle_intent(self, message):
        try:
            r = requests.get("https://status.heroku.com/feed")
            parsed = r.content # TODO parse this RSS feed

            self.speak_dialog("heroku.status", data={'most_recent': "Foo bar baz"})
        except:
            self.speak_dialog("not.found")

    def stop(self):
        pass

def create_skill():
    return HerokuStatusSkill()

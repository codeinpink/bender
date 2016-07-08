from will.plugin import WillPlugin
from will.decorators import hear

class LunchMenuPlugin(WillPlugin):

    menu_URL = "http://iportal.adtran.com/CafeMenu_files/image002.gif"

    @hear("^/bender-lunch-menu")
    def get_lunch_menu(self, message):
        """/bender-lunch-menu: Get this week's lunch menu"""
        self.say(self.menu_URL)

    @hear("^/bender-set-lunch-menu (?P<url>.*)")
    def set_lunch_menu(self, message, url):
        """/bender-set-lunch-menu: Set this week's lunch menu"""
        self.menu_URL = url
        self.say("URL updated!")

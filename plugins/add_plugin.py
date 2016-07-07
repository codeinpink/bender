from will.plugin import WillPlugin
from will.decorators import respond_to, hear

class AddPluginPlugin(WillPlugin):

    @hear("^/bender-add-plugin (?P<code>.*)", multiline=True)
    def add_plugin(self, message, code):
        """add_plugin: Add a plugin to Bender from within HipChat"""
        print(code)
        self.reply(message, "I'm working on it.")

    @hear("^/bender-reload$")
    def reload(self, message):
        """reload: Reload Bender to use new plugins"""
        self.reply(message, "Be back online in a second, baby.")
        # Do stuff here

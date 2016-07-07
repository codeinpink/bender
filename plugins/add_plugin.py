from will.plugin import WillPlugin
from will.decorators import respond_to

class AddPluginPlugin(WillPlugin):

    @respond_to("/bender-add-plugin")
    def add_plugin(self, message):
        """add_plugin: Add a plugin to Bender from within HipChat"""
        self.reply(message, "I'm working on it.")

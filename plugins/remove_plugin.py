from will.plugin import WillPlugin
from will.decorators import hear
import os

class RemovePluginPlugin(WillPlugin):

    @hear("^/bender-remove-plugin (?P<name>.\w+)")
    def remove_plugin(self, message, name):
        """/bender-remove-plugin: Take away one of my plugins from within HipChat"""
        if not name.endswith(".py"):
            name = name + ".py"

        if not os.path.isfile("plugins/{}".format(name)):
            self.reply(message, "Are you trying to get me in trouble? That plugin doesn't exist!")
        else:
            os.remove("plugins/{}".format(name))
            self.reply(message, "Done!")

    @hear("^/bender-remove-plugin help$")
    def help(self, message):
        """/bender-remove-plugin help: See the proper command for removing one of my plugins"""
        self.reply(message, "/bender-remove-plugin my_plugin_file_name")

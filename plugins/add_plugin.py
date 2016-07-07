from will.plugin import WillPlugin
from will.decorators import respond_to, hear

class AddPluginPlugin(WillPlugin):

    @hear("^/bender-add-plugin (?P<name>.\w+) (?P<code>.*)", multiline=True)
    def add_plugin(self, message, name, code):
        """add_plugin: Add a plugin to Bender from within HipChat"""
        self.reply(message, "I'm working on it.")

        with open('plugins/' + name + '.py', 'w+') as f:
            f.write(code)

        self.reply(message, "Done!")

    @hear("^/bender-add-plugin help$")
    def help(self, message):
        """help: See the proper command for adding a plugin to Bender"""
        self.reply(message, "/bender-add-plugin my_plugin_file_name print 'Insert Bender Quote Here'")

from will.plugin import WillPlugin
from will.decorators import respond_to, hear

class AddPluginPlugin(WillPlugin):

    @hear("^/bender-add-plugin (?P<name>.\w+) (?P<code>.*)", multiline=True)
    def add_plugin(self, message, name, code):
        """/bender-add-plugin: Add a plugin to Bender from within HipChat"""
        self.say("I'm working on it.")

        if not name.endswith('.py'):
            name = name + '.py'

        with open('plugins/' + name , 'w+') as f:
            f.write(code)
            self.say("Here's your new plugin, {}".format(name))
            self.say("/code {}".format(code))

        self.reply(message, "Done!")

    @hear("^/bender-add-plugin help$")
    def help(self, message):
        """/bender-add-plugin help: See the proper command for adding a plugin to Bender"""
        self.reply(message, "/bender-add-plugin my_plugin_file_name print 'Insert Bender Quote Here'")

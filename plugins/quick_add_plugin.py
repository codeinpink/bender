from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
class QuickAddPluginPlugin(WillPlugin):

    @hear("^/bender-add-plugin (?P<name>.\w+) (?P<code>.*)", multiline=True)
    def add_plugin(self, message, name, code):
        """add_plugin: Add a plugin to Bender from within HipChat"""
        self.say(message, "I'm working on it.")
	code = quick_wrap_code(messsage, name, code)
        self.say("Here's your new plugin, {}.py".format(name))
        self.say("/code {}".format(code))

	if name.endswith('.py'):
	    with open('plugins/' + name , 'w+') as f:
	        f.write(code)
	else:
            with open('plugins/' + name + '.py', 'w+') as f:
	        f.write(code)

        self.reply(message, "Done!")
	
    def quick_wrap_code(message, name, code):
        code += 'from will.plugin import WillPlugin\n' + \
                 'from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings\n\n' + \
                 'class QuickAddPluginPlugin(WillPlugin):\n' + \
                 '@hear("^{} {}$".format(message, name)'
        return code

    @hear("^/bender-add-plugin help$")
    def help(self, message):
        """help: See the proper command for adding a plugin to Bender"""
        self.reply(message, "/bender-add-plugin my_plugin_file_name print 'Insert Bender Quote Here'")

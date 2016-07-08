from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
class QuickAddPluginPlugin(WillPlugin):

    @hear("^/bender-quick-add-plugin (?P<name>.\w+) (?P<code>.*)", multiline=True)
    def quick_add_plugin(self, message, name, code):
        """quick_add_plugin: Add a plugin to Bender from within HipChat"""
        self.say("I'm working on it.")
	code = self.quick_wrap_code(message, name, code)
        self.say("Here's your new plugin, {}.py".format(name))
        self.say("/code {}".format(code))

	if name.endswith('.py'):
	    with open('plugins/' + name , 'w+') as f:
	        f.write(code)
	else:
            with open('plugins/' + name + '.py', 'w+') as f:
	        f.write(code)

        self.reply(message, "Done!")
	
    def quick_wrap_code(self, message, name, code):
        code_array = code.split('\n')
        print code_array
        code =   '# -*- coding: utf-8 -*-\n' + \
                 'from will.plugin import WillPlugin\n' + \
                 'from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings\n\n' + \
                 'class {}Plugin(WillPlugin):\n'.format(name) + \
                 '    @hear("^/bender-{}")'.format(name) 
        for line_of_code in code_array:
            code += '\n    {}'.format(line_of_code.decode('shift-jis').encode('utf-8'))
        return code

    @hear("^/bender-quick-add-plugin help$")
    def help(self, message):
        """help: See the proper command for adding a plugin to Bender"""
        self.reply(message, "/bender-add-plugin my_plugin_file_name print 'Insert Bender Quote Here'")

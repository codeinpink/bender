from will.plugin import WillPlugin 
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
class AddPluginPlugin(WillPlugin):

    @hear("^/bender-add-plugin\s*(?P<name>.\w+)\s*\n?\s*(?P<code>.*)", multiline=True)
    def add_plugin(self, message, name, code):
        """
           /bender-add-plugin: Add a plugin to me from within HipChat
                             Syntax: /bender-add-plugin {plugin name} {plugin code}
                             How To Call made Plugin: /bender-{plugin name}
        """
	code = self.quick_wrap_code(message, name, code)
        self.say("Look at all this pretty Python you wrote. Just for me :)")
        self.say("/code {}".format(code))

	if name.endswith('.py'):
	    with open('plugins/' + name , 'w+') as f:
	        f.write(code)
	else:
            with open('plugins/' + name + '.py', 'w+') as f:
	        f.write(code)

        self.reply(message, "Reload me! Then you can use the command '/bender-{}' to run your plugin!\n".format(name))
	
    def quick_wrap_code(self, message, name, code):
        code_array = code.split('\n')
        print code_array
        code =   '# -*- coding: utf-8 -*-\n' + \
                 'from will.plugin import WillPlugin\n' + \
                 'from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings\n\n' + \
                 'class {}Plugin(WillPlugin):\n'.format(name) + \
                 '    @hear("^/bender-{}")\n'.format(name) 
        for line_of_code in code_array:
            code += '    {}\n'.format(line_of_code.decode('utf-8').encode('utf-8'))
        return code

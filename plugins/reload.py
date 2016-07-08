from will.plugin import WillPlugin
from will.decorators import hear
import os


class ReloadBenderPlugin(WillPlugin):
    @hear('^/bender-reload$')
    def reload(self, message):
        """/bender-reload: reloads/restarts me."""
        self.say("FYI: I'm going to reload.", message=message)
        os.execl('./restart.sh', '')

from will.plugin import WillPlugin
from will.decorators import hear
import os


class RestartWill(WillPlugin):
    @hear('^/bender-restart$')
    def restart(self, message):
        """restart: restarts Will"""
        self.say("FYI. I'm going to restart", message=message)
        os.system('env -i ./restart.sh')

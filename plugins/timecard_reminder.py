from will.plugin import WillPlugin
from will.decorators import periodic


class TimeCardReminderPlugin(WillPlugin):

	etime_URL = "https://adpeet2.adp.com/101hz2p/navigator/logon"

	@periodic(hour="9", minute="30", day_of_week="fri")
	def reminder(self):
		"""timecard_reminder: Reminds people to fill out their time cards every Friday"""
		self.say("@all Don't forget to fill out your time cards!!  %s" % self.etime_URL)

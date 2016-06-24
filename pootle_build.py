from errbot import BotPlugin, botcmd


class PootleBuild(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """

    @botcmd
    def pootle_build(self, msg, args):
        """
        """
        return 'oh ok, yep on it'

from collections import namedtuple

from twisted.words.protocols import irc
from twisted.internet import protocol
from twisted.internet import reactor

from plugin import pluginsystem
pluginsystem.reload()

Info = namedtuple("Info", ["bot", "user", "channel"])

class Bot(irc.IRCClient):
    nickname = "Somebot" 
    prefix = "#"
    channels = ["bots", "python-forum2"]

    def signedOn(self):
        print "Signed on as %s." % (self.nickname,)
        for channel in self.channels:
            self.join(channel)

    def joined(self, channel):
        print "Joined %s." % (channel,)
        self.msg(channel, "Hello everybody, my command prefix is %s" % self.prefix)

    def privmsg(self, user, channel, msg):
        print msg

        user = user[:user.index("!")]

        # This seems to behave inconsistently between different version of twisted.
        # Therefore I present you this stupid hack.
        if channel == self.nickname:
            channel = None

        is_directed = msg.startswith(self.nickname)
        if is_directed:
            msg = msg.split(" ", 1)[1]

        is_prefixed = msg.startswith(self.prefix)
        if is_prefixed:
            msg = msg[len(self.prefix):]

        if msg and (is_directed or is_prefixed):
            parameters = msg.split()
            command = parameters.pop(0)
            target = channel or user

            info = Info(self, user, channel)
            self.msg(target, pluginsystem.command(info, command, *parameters))

class BotFactory(protocol.ClientFactory):
    protocol = Bot

    def clientConnectionLost(self, connector, reason):
        print "Lost connection (%s), reconnecting." % (reason,)
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "Could not connect: %s" % (reason,)

if __name__ == "__main__":
    bot = BotFactory()
    reactor.connectTCP('irc.freenode.net', 6667, bot)
    reactor.run()

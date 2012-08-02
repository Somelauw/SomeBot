import inspect
from collections import namedtuple

from twisted.words.protocols import irc
from twisted.internet import protocol
from twisted.internet import reactor

import plugin
import plugin.basic
import plugin.web

Info = namedtuple("Info", ["bot", "user", "channel"])

class Bot(irc.IRCClient):
    nickname = "Somebot" 
    prefix = "#"

    def signedOn(self):
        self.join(self.factory.channel)
        print "Signed on as %s." % (self.nickname,)

    def joined(self, channel):
        print "Joined %s." % (channel,)
        self.msg(channel, "Hello everybody, my command prefix is %s" % self.prefix)

    def privmsg(self, user, channel, msg):
        print msg
        is_directed = msg.startswith(self.nickname)
        if is_directed:
            msg = msg.split(maxsplit=1)[1]

        is_prefixed = msg.startswith(self.prefix)
        if is_prefixed:
            msg = msg[len(self.prefix):]

        if msg and (is_directed or is_prefixed):
            parameters = msg.split()
            command = parameters.pop(0)

            try:
                info = Info(self, user, channel)
                self.msg(channel, plugin.commands[command](info, *parameters))
            except KeyError:
                self.msg(channel, "Unknown command #%s" % command)
            except TypeError:
                argspec = inspect.getargspec(plugin.commands[command])
                n_args = len(argspec.args) - 1
                self.msg(channel, "Command #%s takes %d parameters" % (command, n_args))

class BotFactory(protocol.ClientFactory):
    nickname = Bot.nickname
    protocol = Bot

    def __init__(self, channel):
        self.channel = channel

    def clientConnectionLost(self, connector, reason):
        print "Lost connection (%s), reconnecting." % (reason,)
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "Could not connect: %s" % (reason,)

if __name__ == "__main__":
    reactor.connectTCP('irc.freenode.net', 6667, BotFactory("#SomeBot"))
    reactor.connectTCP('irc.freenode.net', 6667, BotFactory("#python-forum"))
    reactor.run()

import os
import imp
import sys
import inspect

class PluginSystem(object):
    def __init__(self):
        self.setup

    def setup(self):
        self.commands = {}
        self.modules = []

        pluginpath = os.path.join(os.path.dirname(imp.find_module("main")[1]), "plugins/")
        pluginfiles = [fname[:-3] for fname in os.listdir(pluginpath) if fname.endswith(".py")]

        if not pluginpath in sys.path:
            sys.path.append(pluginpath)
            self.plugins = [__import__(fname) for fname in pluginfiles]

    def reload(self):
        self.setup()
        for plugin in self.plugins:
            reload(plugin)

    def add_command(self, command):
        self.commands[command.__name__] = command

    def command(self, info, command, *args):
        command_function = self.commands.get(command)
        if command_function:
            argspec = inspect.getargspec(command_function)
            min_args = len(argspec.args) - len(argspec.defaults or ()) - 1
            max_args = len(argspec.args) - 1

            if min_args <= len(args) and (argspec.varargs or len(args) <= max_args):
                return str(self.commands[command](info, *args))
            else:
                return "Command %s takes between %d and %d paramters" %\
                        (command, min_args, max_args)
        else:
            return "Unknown command %s" % command

pluginsystem = PluginSystem()

def add_command(command):
    """Decorator to add commands"""
    pluginsystem.add_command(command)
    return command


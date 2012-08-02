import plugin
from plugin import add_command

@add_command
def source(info):
    """Shows an url to the source"""
    
    return "https://github.com/Somelauw/SomeBot"

@add_command
def help(info, command=None):
    """Get help about this bot"""

    if not command:
        return "Commands: " + ", ".join(plugin.commands.keys())
    else:
        if command.startswith(info.bot.prefix):
            command = command[1:]
        if command in plugin.commands:
            doc = plugin.commands[command].__doc__ or "No help available"
            return doc.split("\n")[0]
        else:
            return "Unknown command %s" % command


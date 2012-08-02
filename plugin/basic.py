import plugin
from plugin import add_command

@add_command
def source(info):
    """Shows an url to the source"""
    
    #return "Not published yet"
    return "https://github.com/Somelauw/SomeBot"

@add_command
def commands(info):
    """Shows available commands"""

    return "Commands: " + ", ".join("#" + command for command in plugin.commands.keys())

@add_command
def help(info, command=None):
    """Get help about a topic"""

    if not command:
        return commands(info)
    else:
        if command.startswith("#"):
            command = command[1:]
        if command in plugin.commands:
            doc = plugin.commands[command].__doc__ or "No help available"
            return doc.split("\n")[0]
        else:
            return "Unknown command #%s" % command


from plugin import add_command
import urllib

@add_command
def google(info, *args):
    """Google something"""

    return "http://google.com/search?q=" + urllib.quote(" ".join(args))

#@add_command
def wiki(info, *args):
    """Search something up on wikipedia"""

    #TODO only return valid wiki's
    return "http://en.wikipedia.org/wiki/" + urllib.quote(" ".join(args))


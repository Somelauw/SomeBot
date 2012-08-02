from plugin import add_command
import urllib

@add_command
def google(info, *args):
    """Google something"""

    return "http://google.com/search?q=" + urllib.quote(" ".join(args))

@add_command
def bing(info, *args):
    """Bing something"""

    return "http://bing.com/search?q=" + urllib.quote(" ".join(args))

@add_command
def duckduckgo(info, *args):
    """Duckduckgo something"""

    return "http://duckduckgo.com/search?q=" + urllib.quote(" ".join(args))

@add_command
def wikipedia(info, *args):
    """Search something up on wikipedia"""

    return "http://en.wikipedia.org/wiki/" + urllib.quote(" ".join(args))


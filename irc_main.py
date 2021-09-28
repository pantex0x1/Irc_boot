from irc_class import *
import os
import random

## IRC Config
server = "irc.root-me.org"  # Provide a valid server IP/Hostname
port = 6667
channel = "#root-me_challenge"
botnick = "candy"
botnickpass = ""
botpass = "<%=  %>"
irc = IRC()
irc.connect(server, port, channel, botnick, botpass, botnickpass)

while True:
    text = irc.get_response()
    print(text)

    if "PRIVMSG" in text and channel in text and "hello" in text:
        irc.send(channel, "Hello!")

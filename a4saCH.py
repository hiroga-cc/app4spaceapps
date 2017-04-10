# coding: UTF-8

import re
import random

import send
import a4saDAO

"""
channel = a4sa
"""

class a4saCH():

    themes = ["Earth", "Space Station", "Technology"]

    def __init__(self):
        self.dao = a4saDAO.a4saDAO()
        self.gen = send.GenJson()

    def switch(self,sender,text):
        if text in ("Yes","Sure"):
            send.send(self.gen.setText(sender, "Me too!!"))
            send.send(self.gen.setOption(sender, "Which category?",self.themes))
        elif text in self.themes:
            send.send(self.gen.setTestPlaneList(sender, self.dao.getAppsByTheme(self,text)))
        else:
            send.send(self.gen.setOption(sender, "Are you interested in space apps??",["Yes", "Sure"]))
        return

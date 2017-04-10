# coding: UTF-8

import re
import random

import send
import a4saDAO

"""
channel = a4sa
"""

class a4saCH():

    def __init__():
        dao = a4saDAO.a4saDAO()
        gen = send.GenJson()

    def switch(self,sender,text):
        if text == ("Yes","True"):
            send.send(self.gen.setText(sender, "Me too!!"))
            send.send(self.gen.setOption(sender, "Which category?",["Earth", "Space Station", "Technology"])
        else :
            send.send(self.gen.setOption(sender, "Are you interested in space apps??",["Yes", "True"])

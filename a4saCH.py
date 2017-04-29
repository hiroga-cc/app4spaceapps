# coding: UTF-8

import re
import random

import os
import requests

import send
import a4saDAO

"""
channel = a4sa
"""

class a4saCH():

    themes = ["earth", "aero", "mars", "solar-system", "space-station", "tech"]

    def __init__(self):
        self.dao = a4saDAO.a4saDAO()
        self.gen = send.GenJson()

    def switch(self,sender,text):
        if text in ("Yes","Sure"):
            send.send(self.gen.setText(sender, "Me too!!"))
            send.send(self.gen.setOption(sender, "Which category?",self.themes))
        elif text in self.themes:
            elements = self.dao.getAppsByTheme(text)
            send.send(self.gen.setText(sender, "{0}, it's interesting.".format(text)))
            send.send(self.gen.setTestPlaneList(sender, elements))
        elif text == ("Hi"):
            send.send(self.gen.setOption(sender, "Are you interested in space apps??",["Yes", "Sure"]))
        else:
            guessed = self.helpMeIBM(text)
            elements = self.dao.getAppsByTheme(guessed)
            print ("help me IBM!")
            send.send(self.gen.setText(sender, "You have an interest in {0}, right?".format(guessed)))
            send.send(self.gen.setTestPlaneList(sender, elements))
        return

    # return theme
    def helpMeIBM(self,text):
        username = os.environ["IBM_NLC_USER"]
        password = os.environ["IBM_NLC_PASS"]
        classifier = os.environ["IBM_NLC_CLSFR"]

        url = "https://gateway.watsonplatform.net/natural-language-classifier/api/v1/classifiers/{}/classify".format(classifier)
        res = requests.get(url, auth=(username,password), params={"text":text})
        return res.json()["top_class"]

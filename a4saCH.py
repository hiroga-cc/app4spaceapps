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
    sugoroku = ["renewable", "whether", "earthquake", "Analysis", "health"]

    def __init__(self):
        self.dao = a4saDAO.a4saDAO()
        self.gen = send.GenJson()

    def switch(self,sender,text):
        # Category
        if text in ("Yes","Sure"):
            send.send(self.gen.setText(sender, "Me too!!"))
            send.send(self.gen.setOption(sender, "Which category?",self.themes))
        elif text in self.themes:
            elements = self.dao.getAppsByTheme(text)
            send.send(self.gen.setText(sender, "{0}, it's interesting.".format(text)))
            send.send(self.gen.setTestPlaneList(sender, elements))
        elif text == ("Hi"):
            send.send(self.gen.setOption(sender, "Are you interested in space apps??",["Yes", "Sure"]))

        # Adventure
        elif text in ("OK!", "GO!", "Help me"):
            send.send(self.gen.setOption(sender, "Which is your challenge?",self.sugoroku))
        elif text in self.sugoroku:
            self.getByWordShowAll(sender,text)
            send.send(self.gen.setOption(sender, "Anything else?",self.sugoroku))
        elif text in ("presentation"):
            send.send(self.gen.setImage(sender,"https://api-2017.spaceappschallenge.org/team-photos/zS7mzkyMcxkaCr52p-c5j1wpTYY%3D/908/fill-1440x600/"))

        # Free Search
        else:
            guessed = self.helpMeIBM(text)
            elements = self.dao.getAppsByTheme(guessed)
            print ("help me IBM!")
            send.send(self.gen.setText(sender, "You have an interest in {0}, right?".format(guessed)))
            send.send(self.gen.setTestPlaneList(sender, elements))
        return

    # send all elements by list format
    def getByWordShowAll(self,sender,text):
        elements = self.dao.getAppsByWord(text)
        for i, elm in enumerate(elements):
            print ("#DEBUG elm")
            print (elm)
            if i%3 == 0:
                data = self.gen.returnPlaneListNoElements(sender)

            tmp = self.gen.returnPlaneListElement(elm["title"], elm["image_url"], elm["subtitle"], elm["url"], elm["fallback_url"])
            data["message"]["attachment"]["payload"]["elements"].append(tmp)
            print ("#DEBUG add MSG to data")
            print (data)
            if i%3 == 2 or i+1 == len(elements):
                send.send(data)
        send.send(self.gen.setText(sender, "Wow, total {0} solutions HIT!".format(str(len(elements)))))

    # return theme
    def helpMeIBM(self,text):
        username = os.environ["IBM_NLC_USER"]
        password = os.environ["IBM_NLC_PASS"]
        classifier = os.environ["IBM_NLC_CLSFR"]

        url = "https://gateway.watsonplatform.net/natural-language-classifier/api/v1/classifiers/{}/classify".format(classifier)
        res = requests.get(url, auth=(username,password), params={"text":text})
        return res.json()["top_class"]

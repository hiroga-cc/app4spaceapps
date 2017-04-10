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
        if text in ("Yes","True"):
            send.send(self.gen.setText(sender, "Me too!!"))
            send.send(self.gen.setOption(sender, "Which category?",self.themes))
        elif text in self.themes:
            return
            # earthを鍵に、候補の名前、imgurl, urlを取得 x3 (これは外部メソッド書く)
            # ここに新種のテンプレートを使ったメッセージ
        elif text == "hoge":
            send.send(self.gen.setTestPlaneList(sender))
        else:
            send.send(self.gen.setOption(sender, "Are you interested in space apps??",["Yes", "True"]))

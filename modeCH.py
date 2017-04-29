# coding: UTF-8

import send
import modeDAO

class modeCH():

    modes = ["space apps", "init"]

    def __init__(self):
        self.dao = modeDAO.modeDAO()
        self.gen = send.GenJson()

    def getMode(self, sender):
        mode=self.dao.getMode(sender)
        return mode

    def switch(self,sender,text):
        if text in self.modes:
            self.dao.changeMode(sender,text)
            send.send(self.gen.setText(sender, "OK, Enjoy!"))
            if text = "space apps":
                send.send(self.gen.setOption(sender, "Are you ready for adventure?",["OK!", "GO!"]))
        else:
            send.send(self.gen.setText(sender, "Hello!!"))
            send.send(self.gen.setOption(sender, "Select Your Mode",self.modes))
        return

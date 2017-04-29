# coding: UTF-8

import send
import modeDAO

class modeCH():

    modes = ["SPACE APPS", "INIT"]

    def __init__(self):
        self.dao = modeDAO.modeDAO()
        self.gen = send.GenJson()

    def getMode(self, sender):
        mode=self.dao.getMode(sender)
        return mode

    def switch(self,sender,text):
        if text in self.modes:
            self.dao.changeMode(sender,mode)
            send.send(self.gen.setText(sender, "Swithed!"))
        else:
            send.send(self.gen.setText(sender, "Hello!!"))
            send.send(self.gen.setOption(sender, "Select Your Mode",modes))
        return

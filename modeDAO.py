# coding: UTF-8

import os
import psycopg2
import urllib.parse

class modeDAO():
    def __init__(self):
        urllib.parse.uses_netloc.append("postgres")
        url = urllib.parse.urlparse(os.environ["DATABASE_URL"])
        self.conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )

    def init(self,sender):
        cur = self.conn.cursor()
        cur.execute("insert into mode (sender, mode, language) values (%s, %s, %s);",(sender, "init", "en"))
        self.conn.commit()

    # senderからmodeを返す
    def getMode(self,sender):
        cur = self.conn.cursor()
        cur.execute("select mode from mode where sender = %s;",[sender])
        result = cur.fetchone()
        if (result == None):
            self.init(sender)
            return "init"
        return result[0]

    def changeMode(self,sender, mode):
        print("start update mode!")
        cur = self.conn.cursor()
        cur.execute("update mode set mode = %s where sender = %s;",(mode, sender))
        self.conn.commit()
        return

    def changeLang(self,sender, language):
        cur = self.conn.cursor()
        cur.execute("update mode set language = %s where sender = %s;",(language, sender))
        self.conn.commit()
        return

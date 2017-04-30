# coding: UTF-8

import os
import psycopg2
import urllib.parse

from datetime import *

# connの確立/ 将来的にはクラス化する

class a4saDAO():
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

    # selectした結果を3件全て返す
    def getAppsByTheme(self,theme):
        cur = self.conn.cursor()
        cur.execute("select name, explanation, imgurl, url from apps where theme = %s order by RANDOM() LIMIT 3;",[theme])
        row = cur.fetchone()
        elements=[]
        while row is not None:
            ele={"title":row[0], "image_url":row[2], "subtitle":row[1], "url":row[3], "fallback_url":"https://2016.spaceappschallenge.org/challenges"}
            elements.append(ele)
            row = cur.fetchone()
        return elements

    # フリーワード検索で結果を全て返す
    def getAppsByWord(self,theme):
      cur = self.conn.cursor()
      cur.execute("select name, explanation, imgurl, url from apps where apps.name like %s or apps.explanation like %s order by RANDOM() ;",['%'+theme+'%','%'+theme+'%'])
      row = cur.fetchone()
      elements=[]
      while row is not None:
          ele={"title":row[0], "image_url":row[2], "subtitle":row[1], "url":row[3], "fallback_url":"https://2016.spaceappschallenge.org/challenges"}
          elements.append(ele)
          row = cur.fetchone()
      return elements


    def select1App(self,sender):
        cur = self.conn.cursor()
        cur.execute("select name from apps where id = %d;",1)
        result = cur.fetchone()
        return result[0]

    def getCounts(self):
        cur = self.conn.cursor()
        cur.execute("select count(*) from apps;")
        result = cur.fetchone()
        return result[0]

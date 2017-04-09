# coding: UTF-8

import os
import psycopg2
import urllib.parse

from datetime import *

# connの確立/ 将来的にはクラス化する
def geneConn():
    urllib.parse.uses_netloc.append("postgres")
    url = urllib.parse.urlparse(os.environ["DATABASE_URL"])
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    return conn


### TEST COMMAND ###

def select1App(sender):
    conn = geneConn()
    cur = conn.cursor()
    cur.execute("select name from apps where id = %d;",1)
    result = cur.fetchone()
    return result[0]

def getCounts():
    conn = geneConn()
    cur = conn.cursor()
    cur.execute("select count(*) from apps;")
    result = cur.fetchone()
    return result[0]

# coding: UTF-8

import json
import os
import requests

"""
Utilitys
要素を受け取り、jsonに詰め込んで返す。
text, image, option等の要素ごとのgeneratorと、dataをsendするものに分けられる。
"""

token = os.environ.get("A4SA_PAGE_ACCESS_TOKEN")

# send message
def send(data): # to FacebookMessanger
    url = 'https://graph.facebook.com/v2.6/me/messages'
    headers = {'content-type': 'application/json'}
    params = {"access_token":token}
    r = requests.post(url, params=params, data=json.dumps(data), headers=headers)

class GenJson():

    def setText(self, sender, text):
        data = {
            "recipient": {
                "id":sender
            },
            "message":  {
              "text":text
            }
        }
        return data

    def setImage(self, sender, imgurl):
        data = {
            "recipient":{
                "id":sender
            },
            "message":{
                "attachment":{
                    "type":"image",
                        "payload":{
                            "url":imgurl
                            }
                        }
                    }
                }
        return data

    def setOption(self, sender, text, option): # optionはlist型などで提供願います。
        data = {
            "recipient":{
                "id":sender
            },
            "message":{
                "text":text,
                "quick_replies":[]
            }
        }
        for word in option:
            data["message"]["quick_replies"].append(
                {"content_type":"text",
                "title":word,
                "payload":word}
            )
        return data

    def returnPlaneListElement(self, title, image_url, subtitle, url, fallback_url):
        return  {
                    "title": title,
                    "image_url": image_url,
                    "subtitle": subtitle,
                    "default_action": {
                        "type": "web_url",
                        "url": url,
                        "messenger_extensions": True,
                        "webview_height_ratio": "tall",
                        "fallback_url": fallback_url
                    }
                }
        # button is not covered

    def setTestPlaneList(self, sender, elements):
        data = {
            "recipient":{ "id": sender },
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "list",
                        "top_element_style": "compact",
                        "elements": [],
                        "buttons": [
                            {
                                "title": "View More",
                                "type": "postback",
                                "payload": "payload"
                            }
                        ]
                    }
                }
            }
        }
        for elm in elements:
            tmp = returnPlaneListElement(elm["title"], elm["image_url"], elm["subtitle"], elm["url"], elm["fallback_url"])
            data["message"]["attachment"]["payload"]["elemtens"].append(tmp)
        return data

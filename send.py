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

    def setTestPlaneList(self, sender):
        return {
          "recipient":{
            "id":sender
          }, "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "list",
                    "top_element_style": "compact",
                    "elements": [
                        {
                            "title": "Classic White T-Shirt",
                            "image_url": "https://peterssendreceiveapp.ngrok.io/img/white-t-shirt.png",
                            "subtitle": "100% Cotton, 200% Comfortable",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://peterssendreceiveapp.ngrok.io/view?item=100",
                                "messenger_extensions": "true",
                                "webview_height_ratio": "tall",
                                "fallback_url": "https://peterssendreceiveapp.ngrok.io/"
                            },
                            "buttons": [
                                {
                                    "title": "Buy",
                                    "type": "web_url",
                                    "url": "https://peterssendreceiveapp.ngrok.io/shop?item=100",
                                    "messenger_extensions": "true",
                                    "webview_height_ratio": "tall",
                                    "fallback_url": "https://peterssendreceiveapp.ngrok.io/"
                                }
                            ]
                        },
                        {
                            "title": "Classic Blue T-Shirt",
                            "image_url": "https://peterssendreceiveapp.ngrok.io/img/blue-t-shirt.png",
                            "subtitle": "100% Cotton, 200% Comfortable",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://peterssendreceiveapp.ngrok.io/view?item=101",
                                "messenger_extensions": "true",
                                "webview_height_ratio": "tall",
                                "fallback_url": "https://peterssendreceiveapp.ngrok.io/"
                            },
                            "buttons": [
                                {
                                    "title": "Buy",
                                    "type": "web_url",
                                    "url": "https://peterssendreceiveapp.ngrok.io/shop?item=101",
                                    "messenger_extensions": "true",
                                    "webview_height_ratio": "tall",
                                    "fallback_url": "https://peterssendreceiveapp.ngrok.io/"
                                }
                            ]
                        },
                        {
                            "title": "Classic Black T-Shirt",
                            "image_url": "https://peterssendreceiveapp.ngrok.io/img/black-t-shirt.png",
                            "subtitle": "100% Cotton, 200% Comfortable",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://peterssendreceiveapp.ngrok.io/view?item=102",
                                "messenger_extensions": "true",
                                "webview_height_ratio": "tall",
                                "fallback_url": "https://peterssendreceiveapp.ngrok.io/"
                            },
                            "buttons": [
                                {
                                    "title": "Buy",
                                    "type": "web_url",
                                    "url": "https://peterssendreceiveapp.ngrok.io/shop?item=102",
                                    "messenger_extensions": "true",
                                    "webview_height_ratio": "tall",
                                    "fallback_url": "https://peterssendreceiveapp.ngrok.io/"
                                }
                            ]
                        },
                        {
                            "title": "Classic Gray T-Shirt",
                            "image_url": "https://peterssendreceiveapp.ngrok.io/img/gray-t-shirt.png",
                            "subtitle": "100% Cotton, 200% Comfortable",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://peterssendreceiveapp.ngrok.io/view?item=103",
                                "messenger_extensions": "true",
                                "webview_height_ratio": "tall",
                                "fallback_url": "https://peterssendreceiveapp.ngrok.io/"
                            },
                            "buttons": [
                                {
                                    "title": "Buy",
                                    "type": "web_url",
                                    "url": "https://peterssendreceiveapp.ngrok.io/shop?item=103",
                                    "messenger_extensions": "true",
                                    "webview_height_ratio": "tall",
                                    "fallback_url": "https://peterssendreceiveapp.ngrok.io/"
                                }
                            ]
                        }
                    ],
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

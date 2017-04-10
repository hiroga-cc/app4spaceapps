# coding: UTF-8

#!/usr/bin/env python
import os.path
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

# import and define tornado-y things
from tornado.options import define
define("port", default=5000, help="run on the given port", type=int)

import json
import send

import a4saDAO

verify_token = os.environ.get("A4SA_PAGE_ACCESS_TOKEN")

# application settings and handle mapping info
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/webhook?", WebHookHandler),
            (r"/view?", ViewHandler), # ex. http://localhost:5000/view
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

# the main page
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if 'GOOGLEANALYTICSID' in os.environ:
            google_analytics_id = os.environ['GOOGLEANALYTICSID']
        else:
            google_analytics_id = False
        self.render(
            "main.html",
            page_title='Heroku Funtimes',
            page_heading='Hi! This is Heroku!',
            google_analytics_id=google_analytics_id,
        )

# Webhook Handler
class WebHookHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_argument("hub.verify_token", "") == verify_token:
            self.write(self.get_argument("hub.challenge", ""));
        else:
            self.write('Error, wrong validation token');
    def post(self):
        data = json.loads(self.request.body.decode())
        print ("*** received data ***")
        print (data) # standard -> OFF
        messaging_events = data["entry"][0]["messaging"]
        text = ""
        time = ""
        for event in messaging_events:
            time = event["timestamp"]
            sender = event["sender"]["id"]
            if ("message" in event and "text" in event["message"]):
                text = event["message"]["text"]
            if len(text) <= 0:
                return
            reply = text + "、です！"
            send.sendMessage(send.setBasicMessage(sender, reply))

# for view
class ViewHandler(tornado.web.RequestHandler):
    def get(self):

        cnt = a4saDAO.getCounts()
        google_analytics_id = False

        self.render(
            "main.html",
            page_title='for View',
            page_heading='Nice! We have {} challenges!!'.format(cnt),
            google_analytics_id=google_analytics_id,
        )

def main():
    print('main started nyan nyan')
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(tornado.options.options.port)

    # start it up
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()

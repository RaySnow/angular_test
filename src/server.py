# coding:utf-8
from datetime import datetime
import json
import tornado
from tornado import web, template
import os

from jinja2 import Environment, FileSystemLoader


templates_folder_path = os.path.join(os.path.dirname(__file__), 'templates')
static_folder_path = os.path.join(os.path.dirname(__file__), 'static')

env = Environment(loader=FileSystemLoader(templates_folder_path), variable_start_string="{*",
                  variable_end_string="*}")


class Jinja2TemplateLoader(template.Loader):
    def _create_template(self, name):
        template = env.get_template(name)
        template.generate = template.render
        return template


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render("index.html")


handlers = [(r"/", MainHandler)]
settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    cookie_secret="__TODO:_HAO_PING_JIA_SECRET__",
    template_loader=Jinja2TemplateLoader(templates_folder_path),
    debug=True
)
application = tornado.web.Application(handlers, **settings)



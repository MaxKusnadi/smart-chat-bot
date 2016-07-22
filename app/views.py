from app import app, api
from app.forms import *
from flask import render_template, make_response, redirect, url_for
from flask_restful import Resource
from app.wolfram import searchWolfram
from app.matcher import Matcher
from app.query_parser import Query_Parser
from app.google import analyze_syntax
from app.constants import *
from app.functions import *
from app.customsearch import *


class Index(Resource):
    def __init__(self):
        self.form = Command()
        self.matcher = Matcher(ALL_FUNCS)
        self.query_parser = Query_Parser()

    def get(self):
        return make_response(render_template('index.html', form=self.form))

    def post(self):
        if self.form.validate_on_submit():
            command = self.form.data['command']
            syntax_json = analyze_syntax(command)
            print(syntax_json)
            query = self.query_parser.parse(syntax_json)
            func = self.matcher.match(query)

            if func:
                result = func()
            else:
                result = searchWolfram(command)

            if len(result) == 0:
                keyword = query.obj
                if not keyword:
                    d = dict()
                    d['type'] = "I don't understand your query"
                    d['text'] = ''
                    result = [d]
                result = searchGoogle(keyword)

            return make_response(render_template('index.html',
                                                 form=self.form,
                                                 result=result))
        return redirect('/')


api.add_resource(Index,
                 '/',
                 endpoint='index')

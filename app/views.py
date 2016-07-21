from app import app, api
from app.forms import *
from flask import render_template, make_response, redirect
from flask_restful import Resource, reqparse
from app.wolfram import searchWolfram


class Index(Resource):
    def __init__(self):
        self.form = Command()
    
    def get(self):
        return make_response(render_template('index.html', form=self.form))

    def post(self):
        if self.form.validate_on_submit():
            command = self.form.data['command']
            result = searchWolfram(command)
            
            return make_response(render_template('index.html',
                                                 form=self.form,
                                                 result=result))
        return redirect('/')


api.add_resource(Index,
                 '/',
                 endpoint='index')

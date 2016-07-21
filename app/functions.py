from app.decorator import *
from app.constants import *

@create(CLASSROOM)
def createAssignment():
    d = dict()
    d['type'] = CREATE_CLASSROOM
    d['text'] = ""
    return [d]

@delete(CLASSROOM)
def deleteAssignment():
    d = dict()
    d['type'] = DELETE_CLASSROOM
    d['text'] = ""
    return [d]

@update(CLASSROOM)
def updateAssignment():
    d = dict()
    d['type'] = UPDATE_CLASSROOM
    d['text'] = ""
    return [d]

@query(CLASSROOM)
def queryAssignment():
    d = dict()
    d['type'] = QUERY_CLASSROOM
    d['text'] = ""
    return [d]

@create(ASSIGNMENT)
def createAssignment():
    d = dict()
    d['type'] = CREATE_ASSIGNMENT
    d['text'] = ""
    return [d]

@delete(ASSIGNMENT)
def deleteAssignment():
    d = dict()
    d['type'] = DELETE_ASSIGNMENT
    d['text'] = ""
    return [d]

@update(ASSIGNMENT)
def updateAssignment():
    d = dict()
    d['type'] = UPDATE_ASSIGNMENT
    d['text'] = ""
    return [d]

@query(ASSIGNMENT)
def queryAssignment():
    d = dict()
    d['type'] = QUERY_ASSIGNMENT
    d['text'] = ""
    return [d]

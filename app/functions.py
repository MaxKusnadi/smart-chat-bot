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

@query(CLASSMATE)
def queryClassmate():
    d = dict()
    d["type"] = QUERY_CLASSMATE
    d["text"] = ""
    return [d]

@create(POST)
def createPost():
    d = dict()
    d["type"] = CREATE_POST
    d["text"] = ""
    return [d]

@delete(POST)
def deletePost():
    d = dict()
    d["type"] = DELETE_POST
    d["text"] = ""
    return [d]

@update(POST)
def updatePost():
    d = dict()
    d["type"] = UPDATE_POST
    d["text"] = ""
    return [d]

@query(POST)
def queryPost():
    d = dict()
    d["type"] = QUERY_POST
    d["text"] = ""
    return [d]

@create(PROFILE)
def createProfile():
    d = dict()
    d["type"] = CREATE_PROFILE
    d["text"] = ""
    return [d]

@delete(PROFILE)
def deleteProfile():
    d = dict()
    d["type"] = DELETE_PROFILE
    d["text"] = ""
    return [d]

@update(PROFILE)
def updateProfile():
    d = dict()
    d["type"] = UPDATE_PROFILE
    d["text"] = ""
    return [d]

@query(PROFILE)
def queryProfile():
    d = dict()
    d["type"] = QUERY_PROFILE
    d["text"] = ""
    return [d]

@update(GRADE)
def updateGrade():
    d = dict()
    d["type"] = UPDATE_GRADE
    d["text"] = ""
    return [d]

@query(GRADE)
def queryGrade():
    d = dict()
    d["type"] = QUERY_GRADE
    d["text"] = ""
    return [d]


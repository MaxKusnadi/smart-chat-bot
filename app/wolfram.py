# from flask import jsonify
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import xml.etree.ElementTree as ET


LINK = "http://api.wolframalpha.com/v2/query?input="
APPID = "&appid=VRH54J-A4H2PAHL7Y"

APPID_GOOGLE = "&cx=015262030262987356770:zjjh5gasbl4"


def convertSpace(query):
    lst = query.split()
    return "%20".join(lst)


def getLink(query):
    return LINK + query + APPID


def getRequest(link):
    r = Request(link)
    return r


def openRequest(request):
    try:
        response = urlopen(request).read().decode("utf-8",
                                                  errors="replace")
    except HTTPError:
        response = None

    return response


def convertToXML(response):
    tree = ET.fromstring(response)
    return tree


def findResult(xml):
    lst = list(filter(lambda x: x.tag == 'pod', xml))
    lst = list(map(lambda x: dictResult(x), lst))
    return lst


def dictResult(element):
    d = dict()
    d['type'] = element.get('title')
    d['text'] = element.find('subpod').find('img').get('src')
    return d


def searchWolfram(query):
    # Preparing request
    q = convertSpace(query)
    link = getLink(q)
    req = getRequest(link)
    response = openRequest(req)

    # Parsing to XML
    xml = convertToXML(response)
    result = findResult(xml)
    return result

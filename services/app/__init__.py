import web, auth
import json, time, datetime, decimal
from config import *

def AlchemyToJSON(item):
    d = {}
    for column in item.__table__.columns:
        value = getattr(item, column.name)
        if isinstance(value, bool) or \
                isinstance(value, long) or \
                isinstance(value, datetime.datetime):
            d[column.name] = value
        else:
            d[column.name] = str(value)

    return json.dumps(d)

def set_headers(allow_cache=False):
    web.header('Content-Type', 'application/json')
    if not allow_cache:
        web.header('Cache-Control', 'no-store, no-cache, must-revalidate')
        web.header('Cache-Control', 'post-check=0, pre-check=0', False)
    web.header('Pragma', 'no-cache')

def setToList(theSet):
    listresults = []
    for item in theSet:
        listresults.append(itemToDict(item))
    return listresults

def iterBetterToJSON(iterbetter):
    return json.dumps(setToList(iterbetter))

def itemToJSON(item):
    listresults = []
    listresults.append(itemToDict(item))
    return json.dumps(listresults)

def itemToDict(item):
    dictitem = dict()
    for key in item.keys():
        if isinstance(item.get(key), datetime.datetime):
            dictitem[key] = "%s" % item.get(key)
        elif isinstance(item.get(key), set):
            dictitem[key] = setToList(item.get(key))
        elif isinstance(item.get(key), decimal.Decimal):
            dictitem[key] = "%f" % item.get(key)
        else:
            dictitem[key] = item.get(key)
    return dictitem

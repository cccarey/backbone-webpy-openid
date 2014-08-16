import json, datetime, decimal
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class JSONBase():
	def toJSON(self):
	    d = {}
	    for column in self.__table__.columns:
	        value = getattr(self, column.name)
	        if isinstance(value, bool) or \
	                isinstance(value, long) or \
	                isinstance(value, datetime.datetime) or \
	                isinstance(value, decimal.Decimal):
	            d[column.name] = value
	        else:
	            d[column.name] = str(value)

	    return json.dumps(d)

import web, auth
import json, time, datetime, decimal
from config import *

def set_headers(allow_cache=False):
    web.header('Content-Type', 'application/json')
    if not allow_cache:
        web.header('Cache-Control', 'no-store, no-cache, must-revalidate')
        web.header('Cache-Control', 'post-check=0, pre-check=0', False)
    web.header('Pragma', 'no-cache')

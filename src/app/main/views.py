#!/usr/bin/env python
#
# views.py
#
# App routes
#
# Mar 31, 2015 - Martin McGreal
#

from flask import render_template, send_from_directory, Response, request
from flask_cors import cross_origin
import re
import json
from . import main

# Create our CORS origins regexp
re_origins = [re.compile(u"http://localhost:*")]


# Utility function
def getresponse(call, *args, **kwargs):
    """Generate a standard response."""
    try:
        response = call(*args, **kwargs)
        if type(response) is dict and 'status' in response:
            return Response(mimetype='application/json',
                    response=json.dumps(response))
        elif response is None:
            return Response(mimetype='application/json',
                    response=json.dumps({'code': 0, 'status': 'OK'}))
        elif isinstance(response, Response):
            return response
        else:
            return Response(mimetype='application/json',
                    response=json.dumps({'code': 0, 'status': 'OK',
                                         'result': response}))
    except Exception as e:
        log.exception("Exception in getresponse")
        return Response(mimetype='application/json',
                    response=json.dumps({'code': 5001, 'status': 'Exception',
                                         'result': str(e.__class__)+':'+str(e)}))


# Routes

# Static route for browser icon
@main.route('/favicon.ico')
@cross_origin(origins=re_origins, supports_credentials=True)
def favicon():
    return send_from_directory('../img/', 'blargh.ico',
                                   mimetype='image/vnd.microsoft.icon')


# Testing route
@main.route('/hello', methods=['GET', 'POST', 'OPTIONS'])
@cross_origin(origins=re_origins, supports_credentials=True)
def checkme():
    """Test WS"""
    # Check authorization
    r, v = auth.authorize()
    if r is False:
        return v

    log.debug("checkme: request data: "+str(request.data))
    log.debug("checkme: request args: "+str(request.args))
    log.debug("checkme: request method: "+str(request.method))
    log.debug("checkme: request path: "+str(request.path))

    return Response(mimetype='application/json',
                    response=json.dumps({'code': 0, 'status': 'OK', 'result': request.data}))



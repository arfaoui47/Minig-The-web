#!/usr/bin/python2.7
# -*- coding: utf-8 -*

import json

_file=open('tweets.json','r')
status_result=_file.read()
status_result=json.loads(status_result)
#status = json.dumps(status_result,indent=1)
status = status_result["statuses"]
print json.dumps(status,indent=1)
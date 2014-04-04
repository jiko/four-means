#!/usr/bin/env python

import os, json

print '{'+json.dumps([fn for fn in os.listdir('./html') if fn[-4:] == 'html'])+"}"

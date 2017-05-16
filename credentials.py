"""
Use $ python credentials.py --noauth_local_webserver
"""
from __future__ import print_function
import httplib2
import os

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


SCOPES = 'https://www.googleapis.com/auth/drive'

home_dir = os.getcwd()
credential_dir = os.path.join(home_dir, '.credentials')
if not os.path.exists(credential_dir):
    os.makedirs(credential_dir)
credential_path = os.path.join(credential_dir,
                                'drive.json')
# access_type="offline" and approval_prompt='force'.
store = Storage(credential_path)
credentials = store.get()
if not credentials or credentials.invalid:
    flow = client.OAuth2WebServerFlow(os.environ.get('CLIENT_ID'),
                                os.environ.get('CLIENT_SECRET'),
                                scope=SCOPES,
                                access_type='offline',
                                approval_prompt='force')
    if flags:
            credentials = tools.run_flow(flow, store, flags)
    else: # Needed only for compatibility with Python 2.6
        credentials = tools.run(flow, store)
    print('Storing credentials to ' + credential_path)

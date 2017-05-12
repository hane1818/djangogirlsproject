from __future__ import print_function
import httplib2
import json
import os

from apiclient import discovery
from googleapiclient.http import MediaFileUpload
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    credential_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

    credentials_json = json.loads(open(credential_path).read())
    credentials = client.OAuth2Credentials(
        credentials_json['access_token'],
        credentials_json['client_id'],
        credentials_json['client_secret'],
        credentials_json['refresh_token'],
        credentials_json['token_expiry'],
        credentials_json['token_uri'],
        'hane'
    )
    return credentials

def main():
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    for up to 10 files.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    file_metadata = {'name' : 'db.sqlite3'}
    media = MediaFileUpload('db.sqlite3',
                            mimetype='application/x-sqlite3')
    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()
    print('File ID: %s' % file.get('id'))

if __name__ == '__main__':
    main()

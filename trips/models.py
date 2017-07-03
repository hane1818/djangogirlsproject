from django.contrib.auth.models import User
from django.db import models

import httplib2
from apiclient import discovery
from googleapiclient.http import MediaFileUpload
from drive import get_credentials

from mysite.settings import FLICKR_STORAGE_OPTIONS


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    contact = models.CharField(blank=True, max_length=15)
    content = models.TextField(blank=True)
    photo = models.FileField(blank=True, upload_to='django-test', storage=gd_storage)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self,
             force_insert=False,
             force_update=False,
             using=None,
             update_fields=None):

        print(dir(self.photo.storage))
        super(Post, self).save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields)

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

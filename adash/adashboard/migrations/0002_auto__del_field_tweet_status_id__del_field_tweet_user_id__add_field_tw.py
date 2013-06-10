# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Tweet.status_id'
        db.delete_column(u'adashboard_tweet', 'status_id')

        # Deleting field 'Tweet.user_id'
        db.delete_column(u'adashboard_tweet', 'user_id')

        # Adding field 'Tweet.status_id_str'
        db.add_column(u'adashboard_tweet', 'status_id_str',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)

        # Adding field 'Tweet.user_id_str'
        db.add_column(u'adashboard_tweet', 'user_id_str',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Tweet.status_id'
        db.add_column(u'adashboard_tweet', 'status_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)

        # Adding field 'Tweet.user_id'
        db.add_column(u'adashboard_tweet', 'user_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)

        # Deleting field 'Tweet.status_id_str'
        db.delete_column(u'adashboard_tweet', 'status_id_str')

        # Deleting field 'Tweet.user_id_str'
        db.delete_column(u'adashboard_tweet', 'user_id_str')


    models = {
        u'adashboard.configuration': {
            'Meta': {'object_name': 'Configuration'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'adashboard.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'favorite_count': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status_id_str': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'status_text': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id_str': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user_profile_image_url': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'user_screen_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['adashboard']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

  def forwards(self, orm):
    # Adding model 'Tweet'
    db.create_table(u'adashboard_tweet', (
      (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
      ('status_id', self.gf('django.db.models.fields.CharField')(max_length=30)),
      ('status_text', self.gf('django.db.models.fields.CharField')(max_length=140)),
      ('favorite_count', self.gf('django.db.models.fields.IntegerField')()),
      ('user_id', self.gf('django.db.models.fields.CharField')(max_length=30)),
      ('user_screen_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
      ('user_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
      ('user_profile_image_url', self.gf('django.db.models.fields.CharField')(max_length=256)),
      ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
      ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
    ))
    db.send_create_signal(u'adashboard', ['Tweet'])

    # Adding model 'Configuration'
    db.create_table(u'adashboard_configuration', (
      (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
      ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
      ('value', self.gf('django.db.models.fields.CharField')(max_length=256)),
      ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
    ))
    db.send_create_signal(u'adashboard', ['Configuration'])


  def backwards(self, orm):
    # Deleting model 'Tweet'
    db.delete_table(u'adashboard_tweet')

    # Deleting model 'Configuration'
    db.delete_table(u'adashboard_configuration')


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
      'status_id': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
      'status_text': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
      'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
      'user_id': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
      'user_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
      'user_profile_image_url': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
      'user_screen_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
    }
  }

  complete_apps = ['adashboard']
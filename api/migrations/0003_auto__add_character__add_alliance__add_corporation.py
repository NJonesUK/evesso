# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Character'
        db.create_table(u'api_character', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('characterID', self.gf('django.db.models.fields.IntegerField')()),
            ('characterName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('corp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Corporation'])),
        ))
        db.send_create_signal(u'api', ['Character'])

        # Adding model 'Alliance'
        db.create_table(u'api_alliance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('allianceID', self.gf('django.db.models.fields.IntegerField')()),
            ('allianceName', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'api', ['Alliance'])

        # Adding model 'Corporation'
        db.create_table(u'api_corporation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('corporationID', self.gf('django.db.models.fields.IntegerField')()),
            ('corporationName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ticker', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('alliance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Alliance'])),
        ))
        db.send_create_signal(u'api', ['Corporation'])


    def backwards(self, orm):
        # Deleting model 'Character'
        db.delete_table(u'api_character')

        # Deleting model 'Alliance'
        db.delete_table(u'api_alliance')

        # Deleting model 'Corporation'
        db.delete_table(u'api_corporation')


    models = {
        u'api.alliance': {
            'Meta': {'object_name': 'Alliance'},
            'allianceID': ('django.db.models.fields.IntegerField', [], {}),
            'allianceName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'api.apikey': {
            'Meta': {'object_name': 'ApiKey'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primary_api_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'userid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vcode': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'api.character': {
            'Meta': {'object_name': 'Character'},
            'characterID': ('django.db.models.fields.IntegerField', [], {}),
            'characterName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'corp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Corporation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'api.corporation': {
            'Meta': {'object_name': 'Corporation'},
            'alliance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Alliance']"}),
            'corporationID': ('django.db.models.fields.IntegerField', [], {}),
            'corporationName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ticker': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['api']
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class ApiKey(models.Model):
    user = models.ForeignKey(User)
    userid = models.CharField(max_length=255)
    vcode = models.CharField(max_length=255)
    valid = models.BooleanField()
    primary_api_key = models.BooleanField()

    class Meta:
        verbose_name = _('API Key')
        verbose_name_plural = _('API Keys')

    def __unicode__(self):
        return unicode(self.userid)


class Alliance(models.Model):
    allianceID = models.IntegerField()
    allianceName = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('MODELNAME')
        verbose_name_plural = _('MODELNAMEs')

    def __unicode__(self):
        pass


class Corporation(models.Model):
    corporationID = models.IntegerField()
    corporationName = models.CharField(max_length=255)
    ticker = models.CharField(max_length=6)
    alliance = models.ForeignKey(Alliance)

    class Meta:
        verbose_name = _('Corporation')
        verbose_name_plural = _('Corporations')

    def __unicode__(self):
        return unicode(self.corporationName)


class Character(models.Model):
    characterID = models.IntegerField()
    characterName = models.CharField(max_length=255)
    corp = models.ForeignKey(Corporation)

    class Meta:
        verbose_name = _('Character')
        verbose_name_plural = _('Characters')

    def __unicode__(self):
        return unicode(self.characterName)


class APICharacters(models.Model):
    api_key = models.ForeignKey(ApiKey)
    character = models.ForeignKey(Character)

    class Meta:
        verbose_name = _('APICharacters')
        verbose_name_plural = _('APICharacterss')

    def __unicode__(self):
        pass

    def characters_on_key(self, api_key):
        mapping = self.objects.filter(api_key=api_key)
        character_list = []
        for map_obj in mapping:
            character_list.append(map_obj.character)
        return character_list

    def character_key(self, character):
        key = self.objects.get(character=character)
        return key

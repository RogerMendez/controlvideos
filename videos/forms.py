#encoding:utf-8
from django.forms import ModelForm
from django import forms
from django.forms.util import ErrorList

from videos.models import Videos, Imagen

class DivErrorList(ErrorList):
    def __unicode__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return u''
        return u'<div class="errorlist">%s</div>' % ''.join([u'<p class="bg-color-red fg-color-white padding5">%s</p>' % e for e in self])


class VideosForm(ModelForm):
    class Meta:
        model = Videos
        exclude = ['user']

class ImagenForm(ModelForm):
    class Meta:
        model = Imagen
        exclude = ['video']

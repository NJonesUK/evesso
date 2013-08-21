from django.forms import ModelForm

from api.models import ApiKey

class APIKeyForm(ModelForm):
    class Meta:
        model = ApiKey
        fields = ('userid', 'vcode')
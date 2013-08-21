import evelink
from django import forms
from django.contrib.auth.models import User
from datetime import date

from models import UserProfile
from api.models import ApiKey

attrs_dict = {'class': 'required'}


class RegisterForm(forms.ModelForm):
    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label="Username",
                                error_messages={'invalid': "This value may contain only letters, numbers and @/./+/-/_ characters."})
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    api_userid = forms.IntegerField(label="API UserID")
    api_vcode = forms.CharField(label="API vCode")

    class Meta:
        model = UserProfile
        exclude = ('user',)

    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        user = User.objects.create_user(username, email, password)
        user.is_staff = False
        user.first_name = self.cleaned_data['firstname']
        user.last_name = self.cleaned_data['lastname']
        user.save()

        api_key = ApiKey()
        api_key.userid = self.cleaned_data['api_userid']
        api_key.vcode = self.cleaned_data['api_vcode']
        api_key.user = user
        api_key.primary_api_key = True
        api_key.valid = False
        api_key.save()

        profile = user.get_profile()
        #profile.member_type = self.cleaned_data['member_type']
        profile.save()

        return user

    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        api_userid = cleaned_data.get("api_userid")
        api_vcode = cleaned_data.get("api_vcode")

        if password and confirm_password:
            # Only do something if both fields are valid so far.
            if password != confirm_password:
                raise forms.ValidationError("Passwords do not match")
        if User.objects.filter(username=cleaned_data.get("username")).count():
            raise forms.ValidationError("Username already exists")
        if (api_userid is None) or (api_vcode is None):
            raise forms.ValidationError("API Key Invalid")

        api = evelink.api.API(api_key=(1781152, '5ik9w9O7aXXqglxyg8Gj4wpCHWKFSIRdzikX0PRXdLgK0BTQiQk020LUlRLLNLrW'))
        account = evelink.account.Account(api=api)

        # Always return the full collection of cleaned data.
        return cleaned_data

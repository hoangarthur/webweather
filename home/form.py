from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
class RegistrationForm(forms.Form):
    username = forms.CharField(label="User Name", max_length= 100)
    email = forms.EmailField()
    password1  =forms.CharField(label="Password 1", max_length= 200, widget= forms.PasswordInput())
    password2  =forms.CharField(label="Password 2", max_length= 200, widget= forms.PasswordInput())
    
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1==password2 and password1:
                return password2
        raise forms.ValidationError("your password 2 should be same with password 1")
    def clean_user(self):
        username = self.cleaned_data('username')
        if re.search(r'^\w+$', username):
            raise forms.ValidationError("User Name should be in Alphabet and number")
        try:
            User.objects.get(userName = username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("This account existed!")
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password1'], email=self.cleaned_data['email'])
from datetime import datetime

from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from .models import UserProfile
from .models import MovieProfile

class MyLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class UserRegisterForm(forms.ModelForm):
    password= forms.CharField(label= "password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)
    class Meta:
        model= User
        fields = ('username','first_name','email','password')
#checking whether it matches
        def clean_password2(self):
            cd= self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Password does not match')
            return cd['password2']




class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieProfile
        fields = ['title', 'description', 'genres', 'director','main_actor', 'duration', 'image', 'video']
# forms.py

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import UserProfile

from django import forms
from .models import UserProfile
from django.core.exceptions import ValidationError
from datetime import datetime

from django import forms
from .models import UserProfile
from django.core.exceptions import ValidationError
from datetime import datetime

class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'mobile', 'dob', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if mobile and (not mobile.isdigit() or len(mobile) != 10):
            raise ValidationError("Mobile number must be 10 digits.")
        return mobile

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if dob:
            age = (datetime.today().date() - dob).days // 365
            if age < 18:
                raise ValidationError("You must be at least 18 years old.")
        return dob

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# forms.py
from django import forms


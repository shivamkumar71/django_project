from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Profile

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, label='First Name')
    last_name = forms.CharField(max_length=30, required=True, label='Last Name')
    email = forms.EmailField(max_length=254, required=True, label='Email')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='Password')
    i_agree = forms.BooleanField(required=True, label='I agree to the terms and conditions')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('A user with that email already exists.')
        return email

class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, label='First Name')
    last_name = forms.CharField(max_length=30, required=True, label='Last Name')
    email = forms.EmailField(max_length=254, required=True, label='Email')
    phone = forms.CharField(max_length=20, required=False, label='Phone')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        user = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        if user and hasattr(user, 'profile'):
            self.fields['phone'].initial = user.profile.phone

    def save(self, commit=True):
        user = super().save(commit)
        phone = self.cleaned_data.get('phone')
        profile, created = Profile.objects.get_or_create(user=user)
        profile.phone = phone
        if commit:
            profile.save()
        return user 
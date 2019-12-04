from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    #email = forms.EmailField(required=True)
    good_domains = ['edu']

    def clean_email(self):
        email_domain = self.cleaned_data['email'].split('.')[-1]
        if email_domain not in self.good_domains:
            raise forms.ValidationError('You need a .edu email address.')
        return self.cleaned_data['email']
        '''data = self.cleaned_data('email')
        if ".edu" not in data:
            raise forms.ValidationError("Must be a .edu email address.")
            return data'''

    class Meta:
        #defines meta data related to RegistrationForm class
        model = User
        fields = (
            'username',
            #'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )
        help_texts = {
            'username': ''
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        #clean_email()
        #user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        #cleaned_data makes sure that the data is safe to be saved in database
        if commit:
            user.save()

        return user

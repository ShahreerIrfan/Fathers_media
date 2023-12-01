# users/forms.py


from django import forms
from .models import CustomUser, UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# This form is for singup (commented by Irfan)
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

# This form is for user profile update
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'cover_photo', 'date_of_birth', 'bio', 'followers']
        widgets = {'followers': forms.CheckboxSelectMultiple}

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['followers'].queryset = self.fields['followers'].queryset.all()

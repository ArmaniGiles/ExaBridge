from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import DevUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = DevUser
        fields = ('email','first_name','last_name','password')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = DevUser
        fields = ('email','first_name','last_name','password')
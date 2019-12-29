from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import DevUser, EmployerAccount

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = DevUser
        fields = ('email','first_name','last_name','password')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = DevUser
        fields = ('email','first_name','last_name','password')

class CustomEmployerCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = EmployerAccount
        fields = ('email','first_name','last_name','password','company_name','job_description')

class CustomEmployerChangeForm(UserChangeForm):

    class Meta:
        model = EmployerAccount
        fields = ('email','first_name','last_name','password','company_name','job_description')
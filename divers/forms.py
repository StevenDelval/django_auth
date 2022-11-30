from django.contrib.auth.forms import UserCreationForm
from . import models

class UserCreationFormCustom(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        fields = ["username","email","password1","password2",]
        model = models.User

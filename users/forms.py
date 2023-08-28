# users form.py
# add 2308231236

from django import forms
from users.models import User, UserImage

# user form
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'user_name',
            'user_age',
        ]

# userImage form
class UserImageForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = [
            'user',
            'image_url',
        ]        

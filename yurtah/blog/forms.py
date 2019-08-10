from django import forms


from .models import User, Blog


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('location', 'birth_date')
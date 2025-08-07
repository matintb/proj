from django import forms
from blog.models import comments
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = comments
        #  fields mean things to get from user
        fields = ['name','email','subject','message', 'Post']

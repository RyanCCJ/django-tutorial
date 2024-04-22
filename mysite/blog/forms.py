from captcha.fields import CaptchaField
from django import forms
from blog import models

class PostForm(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = ['author', 'title', 'slug', 'image', 'content', 'category', 'tags']
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['author'].label = '帳號'
        self.fields['title'].label = '標題'
        self.fields['slug'].label = '網址名'
        self.fields['image'].label = '封面相片'
        self.fields['content'].label = '內文'
        self.fields['category'].label = '分類'
        self.fields['tags'].label = '標籤'
        self.fields['captcha'].label = '我不是機器人'
    
    captcha = CaptchaField()

class LoginForm(forms.Form):
    username = forms.CharField(label='帳號', max_length=20)
    password = forms.CharField(label='密碼', max_length=20, widget=forms.PasswordInput())


from rbac import models
from django import forms
from django.core.exceptions import ValidationError

class UserModelForm(forms.ModelForm):

    confirm_password = forms.CharField(label='确认密码')
    class Meta:
        model = models.UserInfo
        fields = ['name','email','password']

    def __init__(self, *args, **kwargs):
        super(UserModelForm,self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        r_pwd = self.cleaned_data.get('confirm_password')
        if pwd == r_pwd:
            return self.cleaned_data
        else:
            raise ValidationError('两次输入的密码不一致')


class UpdateUserModelForm(forms.ModelForm):

    class Meta:
        model = models.UserInfo
        fields = ['name','email']

    def __init__(self, *args, **kwargs):
        super(UpdateUserModelForm,self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



class ResetUserModelForm(forms.ModelForm):

    confirm_password = forms.CharField(label='确认密码')
    class Meta:
        model = models.UserInfo
        fields = ['password',]

    def __init__(self, *args, **kwargs):
        super(ResetUserModelForm,self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        r_pwd = self.cleaned_data.get('confirm_password')
        if pwd == r_pwd:
            return self.cleaned_data
        else:
            raise ValidationError('两次输入的密码不一致')
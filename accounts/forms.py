#!/usr/bin/python
# -*-coding:utf-8-*-


from django import forms
from fields import PasswordField
# from django.contrib.auth import get_user_model
from accounts.models import CustomUser
from cmdb_auth.models import AuthNode
from assets.models import Host
# project_swan,
# from django.utils.text import capfirst
# from django.utils.translation import ugettext_lazy as _


class CurrentCustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username',
                  'password')


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u"用户名",
        error_messages={'required': u'请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"用户名",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label=u"密码",
        error_messages={'required': u'请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"密码",
            }
        ),
    )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            cleaned_data = super(LoginForm, self).clean()
        return cleaned_data



class ChangePasswordForm(forms.Form):
    """
        A form used to change the password of a user in the admin interface.
    """
    newpassword = PasswordField(required=True, max_length=12, min_length=6)
    renewpassword = PasswordField(required=True, max_length=12, min_length=6)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean(self):
        newpassword = self.cleaned_data.get('newpassword')
        renewpassword = self.cleaned_data.get('renewpassword')
        if newpassword and renewpassword:
            if newpassword != renewpassword:
                raise forms.ValidationError(u"此处必须输入和上栏密码相同的内容")
        return renewpassword

    def save(self, commit=True):
        """
        Saves the new password.
        """
        # print self.user.set_password(self.cleaned_data["newpassword"])
        if commit:
            self.user.save()
        return self.user


class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name']

# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['user_key']



class NewPasswordForm(forms.ModelForm):
    newpassword = PasswordField(required=True, max_length=128, min_length=6, label=u'新密码')
    renewpassword = PasswordField(required=True, max_length=128, min_length=6, label=u'确认密码')

    class Meta:
        model = CustomUser
        fields = ['newpassword', 'renewpassword']


class ResetPasswordForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['email']


class AuthNodeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.business = kwargs.pop('business', None)
        super(AuthNodeForm, self).__init__(*args, **kwargs)
        self.fields['node'].choices = Host.objects.values_list("uuid", "eth1").filter(business=self.business)

    class Meta:
        model = AuthNode
        fields = ['node']

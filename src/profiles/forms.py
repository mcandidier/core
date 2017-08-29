from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AdminPasswordChangeForm


User = get_user_model()


class ProfileCreationForm(UserCreationForm):
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control'}))
    password1 = forms.CharField(max_length=100,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control'}))
    password2 = forms.CharField(max_length=100,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control'}))
    email = forms.EmailField(max_length=200,
                             widget=forms.TextInput(
                                 attrs={
                                     'class': 'form-control'}))
    designation = forms.CharField(max_length=100,
                                  required=False,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'name': 'designation'}))
    mobile = forms.CharField(max_length=100,
                             required=False,
                             widget=forms.TextInput(
                                 attrs={
                                     'class': 'form-control',
                                     'name': 'mobile'}))
    direct_line = forms.CharField(max_length=100,
                                  required=False,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'name': 'direct_line'}))
    other_phone = forms.CharField(max_length=100,
                                  required=False,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'name': 'other_phone'}))
    fax = forms.CharField(max_length=100,
                          required=False,
                          widget=forms.TextInput(
                              attrs={
                                  'class': 'form-control',
                                  'name': 'fax'}))
    notes = forms.CharField(max_length=100,
                            required=False,
                            widget=forms.Textarea(
                                attrs={
                                    'class': 'form-control',
                                    'name': 'notes',
                                    'rows': '5'}))

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
            'designation',
            'mobile',
            'direct_line',
            'other_phone',
            'fax',
            'notes'
        )

    def save(self, commit=True):
        user = super(ProfileCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.designation = self.cleaned_data['designation']
        user.mobile = self.cleaned_data['mobile']
        user.direct_line = self.cleaned_data['direct_line']
        user.other_phone = self.cleaned_data['other_phone']
        user.fax = self.cleaned_data['fax']
        user.notes = self.cleaned_data['notes']

        if commit:
            user.save()
        return user


class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control'}))
    email = forms.EmailField(max_length=200,
                             widget=forms.TextInput(
                                 attrs={
                                     'class': 'form-control'}))
    designation = forms.CharField(max_length=100,
                                  required=False,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'name': 'designation'}))
    mobile = forms.CharField(max_length=100,
                             required=False,
                             widget=forms.TextInput(
                                 attrs={
                                     'class': 'form-control',
                                     'name': 'mobile'}))
    direct_line = forms.CharField(max_length=100,
                                  required=False,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'name': 'direct_line'}))
    other_phone = forms.CharField(max_length=100,
                                  required=False,
                                  widget=forms.TextInput(
                                      attrs={
                                          'class': 'form-control',
                                          'name': 'other_phone'}))
    fax = forms.CharField(max_length=100,
                          required=False,
                          widget=forms.TextInput(
                              attrs={
                                  'class': 'form-control',
                                  'name': 'fax'}))
    notes = forms.CharField(max_length=100,
                            required=False,
                            widget=forms.Textarea(
                                attrs={
                                    'class': 'form-control',
                                    'name': 'notes',
                                    'rows': '5'}))

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'designation',
            'mobile',
            'direct_line',
            'other_phone',
            'fax',
            'notes'
        )


class AdminEditPasswordForm(AdminPasswordChangeForm):
    password1 = forms.CharField(max_length=100,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control'}))
    password2 = forms.CharField(max_length=100,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'password1',
            'password2'
        )

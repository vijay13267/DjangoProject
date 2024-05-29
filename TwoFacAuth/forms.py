from django import forms


# creating a form
# class InputForm(forms.Form):
#     email = forms.EmailField(label='Enter your email')


class OTPForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)


class EmailForm(forms.Form):
    email = forms.EmailField(label='Enter your email')
from django.contrib.auth.models import User
from .models import Questions, Answers, Likes
from django import forms


class Login_Form(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class AddQuestionsForm(forms.ModelForm):

    class Meta:
        model = Questions
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Ask ur Question here...', 'rows': 2}),
        }


class AddAnswersForm(forms.ModelForm):

    class Meta:
        model = Answers
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': "Write ur answer here...", 'rows': 4}),
        }

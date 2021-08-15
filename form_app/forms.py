from django import forms
from django.forms import fields

from .models import Choice, Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("content",)


class QuestionDeleteForm:
    # csrfトークンのみ確認
    pass


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ("content",)

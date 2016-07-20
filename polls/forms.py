from django import forms
from .models import Question 
class MyForm(forms.ModelForm):
    class meta:
        model = Question
        

        

    
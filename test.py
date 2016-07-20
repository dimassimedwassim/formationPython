from django.forms import ModelForm
from polls.models import Question

# Create the form class.
class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text','pub_date']

# Creating a form to add an article.
form = QuestionForm()

# Creating a form to change an existing article.
q = Question.objects.get(pk=1)
form = QuestionForm(instance=q)
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect , HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from .forms import MyForm
from .models import Choice, Question
from django.core.mail import send_mail

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
            return Question.objects.order_by('-pub_date')[:5]       
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
def ResultsView(request,pk):
    
    if request.method == 'POST':
            # create a form instance and populate it with data from the request:
        form = MyForm(request.POST)
            # check whether it's valid:
        return HttpResponse('/thanks/')
        # if a GET (or any other method) we'll create a blank form
    else:
        form = MyForm()
        
    return render(request, 'polls/name.html', {'form': form , 'pk':pk})
        
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html', {
            'question' : quesion,
            'error_message' : "you did,'t select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
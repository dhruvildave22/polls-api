from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.generic.edit import CreateView 


from .models import Poll, GeeksModel


def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {"results": list(polls.values("question", "created_by__username",
                                         "pub_date"))}
    return JsonResponse(data)


def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"results": {
        "question": poll.question,
        "created_by": poll.created_by.username,
        "pub_date": poll.pub_date
    }}
    return JsonResponse(data)

class GeeksCreate(CreateView): 
  
    # specify the model for create view 
    model = GeeksModel 
  
    # specify the fields to be displayed 
  
    fields = ['title', 'description'] 


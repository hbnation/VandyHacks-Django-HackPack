from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Event, Role

#don't worry about no objects
def index(request):
    event_list = Event.objects.order_by('date')[:5]
    context = {'event_list': event_list}
    return render(request, 'signup/index.html', context)

def detail(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("Event doesn't exist")
    return render(request, 'signup/detail.html', {'event': event})

def vote(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    try:
        selected_role = event.role_set.get(pk=request.POST['role'])
    except (KeyError, Role.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'signup/detail.html', {
            'event': event,
            'error_message': "You didn't select a role.",
        })
    else:
        selected_role.selection += 1
        selected_role.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('detail', args=(event.id,)))

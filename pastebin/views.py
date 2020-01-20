from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.urls import reverse

from .models import Paste

# Create your views here.

def index(request):
    """
    Website index.
    """
    latest_paste_list = Paste.objects.order_by('-pub_date')[:5]
    context = {'latest_paste_list': latest_paste_list}
    return render(request, 'pastebin/index.html', context)

def paste(request, paste_id):
    try:
        req_paste = Paste.objects.get(pk=paste_id)
    except ValidationError:
        raise Http404("Paste does not exist")
    return render(request, 'pastebin/paste.html', {'paste': req_paste})

def create_form(request):
    return render(request, 'pastebin/make_paste.html')

def confirm_paste(request):
    title = request.POST['title']
    text = request.POST['paste']
    user = request.POST['user']

    paste = Paste(title=title, text=text, pub_date=timezone.now(), pub_user=user)
    paste.save()
    return HttpResponseRedirect(reverse('pastebin:paste', args=(paste.paste_id,)))

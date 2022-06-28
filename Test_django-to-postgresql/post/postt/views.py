from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.urls import reverse
from django.views.generic import UpdateView, DeleteView

def kurs_f(request):
    kurs_p=kurs.objects.all()
    form=AddkursForm(request.POST)
    if request.method == 'POST':
        form = AddkursForm(request.POST)
        if form.is_valid():
            form.save()
            form = AddkursForm()
            return HttpResponseRedirect(reverse('kurs'))
    context={
        'kurs_p':kurs_p,
        'form':form,
    }
    return render(request, "postt/postt.html", context=context)

class update_row(UpdateView):
    model = kurs
    form_class=AddkursForm
    success_url = '/'
    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse('kurs'))
        else:
            return super(update_row, self).post(request, *args, **kwargs)

class delete_row(DeleteView):
    model = kurs
    success_url = '/'
    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse('kurs'))
        else:
            return super(delete_row, self).post(request, *args, **kwargs)

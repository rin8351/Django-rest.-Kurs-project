from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from .models import *
from .forms import *
from django.urls import reverse
from django.views.generic import UpdateView, DeleteView, CreateView

def kurs_f(request):
    if request.user.is_authenticated:
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
    else:
        return HttpResponseRedirect(reverse('login'))

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

class Login(LoginView):
    form = AuthenticationForm
    template_name = 'postt/login.html'

    def get_success_url(self):
        return reverse('kurs')

    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)        
        return context

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")

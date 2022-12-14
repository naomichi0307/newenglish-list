from dataclasses import dataclass, fields
from distutils.core import run_setup
import http
from django.views.generic import ListView, DetailView,CreateView, DeleteView, UpdateView, FormView, TemplateView
from .models import elModel,Newword
from django.urls import reverse_lazy
import requests
import bs4
from selenium import webdriver
from django.shortcuts import render, get_object_or_404
from .forms import VenueForm
from django.http import HttpResponseRedirect
from twisted.internet import reactor
import os, signal
from django.db.models import F
from django.core.exceptions import ValidationError
# Create your views here.


def get_word(query: str) -> str:
    try:
        resp = requests.get(f'https://ejje.weblio.jp/content/{query}', headers={
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        }, verify=False)

        resp.raise_for_status()
        soup = bs4.BeautifulSoup(resp.text, 'html.parser')
        return soup.find(class_='content-explanation').get_text(strip=True)
    except: 
        return "not_http"
class englishlist(ListView):
    template_name='list.html'
    #
    #template_name = 'list_info.html'
    #template_name = 'list_success.html'
    model= Newword

class Englishlist_danger(ListView):
    template_name = 'list_danger.html'
    model = Newword

class Englishlist_info(ListView):
    template_name = 'list_info.html'
    model = Newword

class Englishlist_success(ListView):
    template_name = 'list_success.html'
    model = Newword

class englishdetail(DetailView):
    template_name= 'detail.html'
    model= Newword

def add_venue(request):
    submitted = ('submitted' in request.GET)
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            if not Newword.objects.filter(word=word).exists():
                explanation = get_word(word)
                if explanation == "not_http":
                    return HttpResponseRedirect('/form/')
                # (do something with `explanation` probably?)
                print(explanation)
                form.save()
                result = Newword.objects.get(word=word)
                result.mean = explanation
                result.priority = 'success'
                result.save()

            else:
                result = Newword.objects.get(word=word)
                print(result.pk)
                print(result)
                result.useful = result.useful + 1
                print(result.useful)
                if result.useful >= 15:
                    result.priority = 'danger'
                elif result.useful >= 8:
                    result.priority = 'info'
                result.save()
            return HttpResponseRedirect('/detail/' + str(result.pk))
        raise form.ValidationError('???????????????????????????????????????')
    else:
        form = VenueForm()

    return render(request, 'form.html', {'form': form, 'submitted': submitted})
class englishcreate(CreateView):
    template_name= 'create.html'
    model=Newword
    fields = ('word', 'priority')    # items = elModel.objects.get(word = 'word')
    # print(items)
    success_url = reverse_lazy('list')

class englishdelete(DeleteView):
    template_name = 'delete.html'
    model=Newword
    success_url= reverse_lazy('list')

class englishupdate(UpdateView):
    template_name = 'update.html'
    model = Newword
    fields = ('priority',)
    success_url = reverse_lazy('list')

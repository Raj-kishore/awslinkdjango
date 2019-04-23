from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render
from django.template import loader
from django import forms
from django.http import HttpResponseRedirect
import datetime

def costume_ner(request):
    template = loader.get_template('product/costume_ner.html')
    context = {
        'latest_question_list': "welcome",
    }
    return HttpResponse(template.render(context, request))
def dialogue_mapping(request):
    template = loader.get_template('product/dialogue_mapping.html')
    context = {
        'latest_question_list': "welcome",
    }
    return HttpResponse(template.render(context, request))
def index(request):
    template = loader.get_template('product/index.html')
    context = {
        'latest_question_list': "welcome",
    }
    return HttpResponse(template.render(context, request))
def intent_training(request):
    template = loader.get_template('product/intent_training.html')
    context = {
        'latest_question_list': "welcome",
    }
    return HttpResponse(template.render(context, request))
def login(request):
    template = loader.get_template('product/login.html')
    context = {
        'latest_question_list': "welcome",
    }
    return HttpResponse(template.render(context, request))
def profile(request):
    template = loader.get_template('product/profile.html')
    context = {
        'latest_question_list': "welcome",
    }
    return HttpResponse(template.render(context, request))
def register(request):
    template = loader.get_template('product/register.html')
    context = {
        'latest_question_list': "welcome",
    }
    return HttpResponse(template.render(context, request))
def roll_out(request):
    template = loader.get_template('product/roll_out.html')
    context = {
        'latest_question_list': "welcome",
    }
    return HttpResponse(template.render(context, request))
def test_bot(request):
    template = loader.get_template('product/test_bot.html')
    context = {
        'latest_question_list': "welcome",
    }
    return HttpResponse(template.render(context, request))

def leftbar(request):
    template = loader.get_template('product/parts/leftbar.html')
    context = {
        'latest_question_list': "welcome",
    }
    return HttpResponse(template.render(context, request))
def realtime(request):
    template = loader.get_template('product/parts/demo.html')
    context = {
        'latest_question_list': "welcome",
    }
    return HttpResponse(template.render(context, request))
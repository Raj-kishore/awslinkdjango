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
    template = loader.get_template('constructiondemo/404.html')
    context = {
        'latest_question_list': "welcome",
    }
    return HttpResponse(template.render(context, request))
def dialogue_mapping(request):
    template = loader.get_template('constructiondemo/blog-archive.html')
    context = {
        'latest_question_list': "welcome",
    }
    return HttpResponse(template.render(context, request))
def index(request):
    template = loader.get_template('constructiondemo/index.html')
    context = {
        'latest_question_list': "welcome",
    }
    return HttpResponse(template.render(context, request))
def intent_training(request):
    template = loader.get_template('constructiondemo/blog-single.html')
    context = {
        'latest_question_list': "welcome",
    }
    return HttpResponse(template.render(context, request))
def login(request):
    template = loader.get_template('constructiondemo/contact.html')
    context = {
        'latest_question_list': "welcome",
    }
    return HttpResponse(template.render(context, request))
def register(request):
    template = loader.get_template('constructiondemo/course-detail.html')
    context = {
        'latest_question_list': "welcome",
    }
    return HttpResponse(template.render(context, request))
def roll_out(request):
    template = loader.get_template('constructiondemo/course.html')
    context = {
        'latest_question_list': "welcome",
    }
    return HttpResponse(template.render(context, request))
def test_bot(request):
    template = loader.get_template('constructiondemo/gallery.html')
    context = {
        'latest_question_list': "welcome",
    }
    return HttpResponse(template.render(context, request))

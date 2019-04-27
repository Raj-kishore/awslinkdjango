

from django.urls import path

from . import views

urlpatterns = [
path('', views.index),
path('index', views.index),
path('404', views.costume_ner),
path('blog-archive', views.dialogue_mapping),
path('blog-single', views.intent_training),
path('contact', views.login),
path('course-detail', views.register),
path('course', views.roll_out),
path('gallery', views.test_bot)
]
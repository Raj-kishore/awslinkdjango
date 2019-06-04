from django.urls import path

from . import views

urlpatterns = [
path('', views.index),
path('entities', views.costume_ner),
path('dialoguemap', views.dialogue_mapping),
path('intents', views.intent_training),
path('login', views.login),
path('register', views.register),
path('rollout', views.roll_out),
path('demo', views.test_bot),
path('profile', views.profile),
path('leftbar', views.leftbar),
path('realtime', views.realtime),
path('your-name', views.get_name)
]
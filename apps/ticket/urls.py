from django.conf.urls import url
from . import views # . means the current folder

app_name = "ticket"

urlpatterns = [
    url(r'^$', views.index, name="index"), # localhost:8000/ticket/
    url(r'^new', views.new, name="new"), 
    url(r'^all', views.all, name='all'), 
    url(r'^notification/$', views.notify, name='notify')
]
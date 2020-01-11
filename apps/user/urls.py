from django.conf.urls import url
from . import views # . means the current folder

app_name = "user"

urlpatterns = [
    url(r'^$', views.index, name="index"), # r'$' looks for an empty string after localhost:8000
    url(r'^login', views.login_page, name="login_page"),
    url(r'^register', views.register_page, name="register_page"),
    url(r'^create/$', views.create, name='create'),
    url(r'^log/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^edit/$', views.edit, name="edit"),
    url(r'^update/$', views.update, name="update")
]
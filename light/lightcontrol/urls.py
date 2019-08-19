from django.conf.urls import url
from django.urls import path
from lightcontrol import views

urlpatterns = [
	path('',views.index_view,name='index'),
]

from django.conf.urls import include, url
from .views import *

urlpatterns = [
	url(r'^$',Welcome_View.as_view()),
]
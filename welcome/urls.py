from django.urls import path
from . import views

app_name='welcome'

urlpatterns = [
	path('', views.home),
	path('/teacher/',views.teacher,name="teacher"),
    path('/new_subject/',views.new_subject,name="new_subject"),
]
# from django.conf.urls import url
from first_app import views
from django.urls import path

app_name = 'first_app'

urlpatterns = [
    path("", views.index, name='index'),
    path("find_train/", views.find_train, name='find_train'),
    path("find_train/results", views.result, name="result"),
]

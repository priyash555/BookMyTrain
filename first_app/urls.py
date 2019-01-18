# from django.conf.urls import url
from first_app import views
from django.urls import path
from django.contrib import admin

app_name = 'first_app'

urlpatterns = [
    path("", views.index, name='index'),
    path("find_train/", views.find_train, name='find_train'),
    path("find_train/result/", views.result, name="result"),
    path('admin/', admin.site.urls),
]

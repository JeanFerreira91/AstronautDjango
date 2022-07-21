from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('idom-page/', views.index2, name='index2'),
    path('slider-page/', views.index3, name='index3'),
]

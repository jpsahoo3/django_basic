from django.urls import path
from . import views

urlpatterns = [
    path('', views.myfunction, name = 'index'),
    path('about', views.myfunctionabout, name = 'about'),
    path('intro/<str:name>/<int:age>', views.intro, name = 'intro'),
    path('myfirstpage', views.myfirstpage, name='myfirstpage'),
    path('mysecondpage', views.mysecondpage, name='mysecondpage'),
    path('mythirdpage', views.mythirdpage, name='mythirdpage'),
    path('myimage', views.myimage, name='myimage'),
    path('myimage2', views.myimage2, name='myimage2'),
    path('myimage3', views.myimage3, name='myimage3'),
    path('myimage4', views.myimage4, name='myimage4'),
    path('myimage5/<str:imagename>', views.myimage5, name='myimage5'),
    path('myform', views.myform, name='myform'),
    path('submitmyform', views.submitmyform, name='submitmyform'),
    path('myform2', views.myform2, name='myform2'),
]
from django.urls import path,include
from . import views
urlpatterns = [
    path('heloo',views.TestFun,name='heloo'),
    path('about',views.AboutFun,name='about'),
    path('sample',views.SamFun,name='sample')
]
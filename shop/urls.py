from django.urls import path,include
from.views import*
from . import views
urlpatterns = [
    path('',home),
    path('show/<int:adad>', views.show, name='show'),
    

]



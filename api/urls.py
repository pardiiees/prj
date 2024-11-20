from django.urls import path,include
from .views import *
from rest_framework.authtoken import views
urlpatterns = [
    path('product/',ProductList.as_view()),
    path('product/create/',ProductList.as_view()),
    path('product/update/',ProductList.as_view()),
    path('product/delete/',ProductList.as_view()),
    path('product/<adad>',ProductDetail.as_view()),
    path('login/',views.obtain_auth_token),

   

]

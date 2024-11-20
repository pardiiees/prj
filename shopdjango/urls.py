from django.contrib import admin
from django.urls import path, include
from shop.views import *
from django.conf.urls.static import static
from django.conf import settings

# from azbankgateways.urls import az_bank_gateways_urls


urlpatterns = [
    path('admin', admin.site.urls),
    # path('bankgateways/', az_bank_gateways_urls()),
    path('request/<fkpk>', send_request, name='request'),
    path('verify/', verify , name='verify'),
    path('', home),
    path('products', product, name='product'),
    path('sabad', vsabad),
    path('shop', include("shop.urls")),
    path('contact', contact),
    path('product', product, name="product"),
    path('users', users),
    path('userspanel', upanel),
    path('error', error),
    path('register', reg),
    path('logout', lout),
    path('success', sc),
    path('addtocart/<adad>',addtocart, name="addtocart"),
    path('delcart/<adad>',delcart),
    path('editqnt/<adad>',editqnt),
    path('buy/<pk>', buy),
    path('api/', include('api.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from shop.models import product
from shop.models import category
from .serializers import ProductSerializer

# Create your views here.
class ProductList(APIView):
    authentication_classes=(TokenAuthentication,)
    def get(self,request):
        if request.user.is_authenticated:
            q=product.objects.all()
            ser=ProductSerializer(instance=q,many=True)
            return Response(ser.data)
        else:
            return  Response({"message":":(توکن برای نمایش وجود ندارد"},status=401)




    def post(self,request):
        if request.user.is_authenticated:
            request.data._mutable = True
            findcategory = category.objects.filter(onvan= request.data["category"])
           
            request.data["category"]= findcategory.values()[0]['id']
            print(findcategory.values())
            ser=ProductSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({"status":"success"},status=201)
            return Response(ser.errors)
        else:
            return  Response({"message":":(توکن برای ایجاد کردن وجود ندارد"},status=401)
        
    
    def put(self,request):
        if request.user.is_authenticated:
            i=product.objects.get(id=request.data['id'])
            ser=ProductSerializer(data=request.data,instance=i,partial=True)
            if ser.is_valid():
                ser.save()
                return Response({"status":"success"},status=201)
            return Response(ser.errors)
        else:
            return  Response({"message":":(توکن برای به روز کردن وجود ندارد"},status=401)


    def delete(self,request):

            i=product.objects.get(id=request.data['id'])
            i.delete()
            return Response({"status":"success"})

        

class ProductDetail(APIView):
    authentication_classes=(TokenAuthentication,)
    def get(self,request,adad):
        if request.user.is_authenticated:
            q=product.objects.get(id=adad)
            ser=ProductSerializer(instance=q)
            return Response(ser.data)
        else:
            return  Response({"message":":(توکن برای نمایش وجود ندارد"},status=401)


from django.db import models
from django.conf import settings
import datetime 
from .models import*
from django.contrib.auth.models import  User

# Create your models here.

class category(models.Model):
    onvan=models.CharField(max_length=30,verbose_name="دسته")
    def __str__(self)-> str:
        return self.onvan


class product(models.Model):
    onvan=models.CharField(max_length=30,verbose_name="نام محصول")
    category = models.ManyToManyField(to=category)
    gheymat=models.DecimalField(max_digits=10,decimal_places=0,verbose_name="قیمت")
    off=models.IntegerField(default=1,verbose_name="تخفیف")
    aks=models.ImageField(upload_to='shop/static/shop/assets/images/aks',verbose_name="عکس")
    tosif=models.TextField(verbose_name="توصیف")
    noe=models.IntegerField(default=1)
    is_special = models.BooleanField(null=True, verbose_name="فروش ویژه")
    special_price=models.DecimalField(max_digits=10,decimal_places=0,null=True,verbose_name=" قیمت ویژه")
    def __str__(self):
        return self.onvan

    
class akss(models.Model):
    related_mahsool = models.ForeignKey(product, on_delete=models.CASCADE, related_name='img')
    akss=models.ImageField(upload_to='shop/static/shop/assets/images/img')
    noe=models.IntegerField(default=1)
    

class contact(models.Model):
    name=models.CharField(max_length=30,verbose_name="نام")
    email=models.CharField(max_length=50,verbose_name="ایمیل")
    text=models.CharField(max_length=500,verbose_name="متن")


class client(models.Model):
    firstname=models.CharField(max_length=30,verbose_name="نام")
    lastname=models.CharField(max_length=30,verbose_name="نام خانوادگی")
    username=models.CharField(max_length=30,verbose_name=" نام کاربری")
    password=models.CharField(max_length=30,verbose_name="رمز عبور")
    class Meta:
        verbose_name="مشتری"
        verbose_name_plural="مشتریان"
    def __str__(self)-> str:
        return f"{self.username}"
    



class sabad(models.Model):
    client=models.ForeignKey(client,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    qnt=models.IntegerField()

    def __str__(self):
        return f"sabad Item: {self.product.onvan} ({self.qnt})"






class faktor(models.Model):
    client=models.ForeignKey(client,on_delete=models.CASCADE)
    date=models.DateTimeField(default=datetime.datetime.now) 
    totalprice=models.DecimalField(max_digits=10,decimal_places=0) 
    # details = models.OneToOneField(faktor_details)
    ispaid = models.BooleanField(default=False)
    def __str__(self)-> str:
        return self.client.username 

class faktor_details(models.Model):
    faktor=models.ForeignKey(faktor,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    qnt=models.IntegerField()
    sent = models.BooleanField(default=False)
    # ispaid = models.BooleanField(default=False)
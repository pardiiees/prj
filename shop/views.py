from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import contact as cn
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.models import  User
from .models import *
from .forms import *
from django.db.models import Q
from .models import product as prd

import requests
import json



if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'


ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

description = "tozih"

CallbackURL = 'http://127.0.0.1:8000/verify/'
amount = 100000

def send_request(request,fkpk):
    fk = faktor.objects.get(pk= fkpk)
    amount = int(fk.totalprice) *10
    


    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount * 10,
        "Description": description,
        # "Phone": phone,
        "CallbackURL": CallbackURL,
    }

    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    try:
        response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                return redirect(ZP_API_STARTPAY + str(response['Authority']))
            else:
                return HttpResponse({'status': False, 'code': str(response['Status'])})
        return HttpResponse(response)

    except requests.exceptions.Timeout:
        return HttpResponse({'status': False, 'code': 'timeout'})
    except requests.exceptions.ConnectionError:
        return HttpResponse({'status': False, 'code': 'connection error'})



def verify(request):
    authority = request.GET.get('authority')
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Authority": authority,
    }
    data = json.dumps(data)
    headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
    response = requests.post(ZP_API_VERIFY, data=data,headers=headers)
    res = HttpResponse(response)
    if res.status_code == 200:

    
        response = response.json()
        if response['Status'] == 100:
            return {'status': True, 'RefID': response['RefID']}
        else:
            return {'status': False, 'code': str(response['Status'])}
        
    return response




def product(request):
    tt = request.GET.get("tt")
    p = prd.objects.all()

    if tt:
        p = p.filter(Q(onvan__icontains=tt) | Q(tosif__icontains=tt))

    p = p.distinct()

    l1 = p.filter(noe=1)
    l2 = p.filter(noe=2)
    l3 = p.filter(noe=3)
    l4 = p.filter(noe=4)

    return render(request, "shop/products.html", context={"mahsoolat": l1, "ganebi": l2, "printer": l3, "micro_sd": l4})






def contact(request):
    n=request.GET.get("name")
    e=request.GET.get("email")
    t=request.GET.get("text")
    if(n):
        cn.objects.create(name=n,email=e,text=t)
        return render(request,"shop/s.html")
    f=ContactForm()
    return render(request,"shop/contact.html",{"f":f})

def show(request,adad):
    l=prd.objects.get(id=adad)
    aks_list=akss.objects.filter(related_mahsool_id=adad)
    return render(request, "shop/show.html",context={"mahsool":l,"aks_list":aks_list})

def home(request):
    p=prd.objects.all  
    if 'login' in request.session:
        return render(request, "shop/index.html", context={"p": p})
    else:
        return render(request, "shop/index.html", context={"p": p})
  

def addtocart(request,adad):
    if (request.session.get("login")):
        cl=client.objects.get(username=request.session["login"])
        pr=prd.objects.get(id=adad)
        sb=sabad.objects.filter(client=cl,product=pr).first()
        if sb==None:
            sabad.objects.create(client=cl,product=pr,qnt=1)
        else:
            sb.qnt=sb.qnt+1
            sb.save()
        sb=sabad.objects.filter(client=cl,product=pr).first()
        request.session['cartImage'] = sb.product.aks.name
        print(sb.qnt)
        request.session['cartqnt'] = sb.qnt
        request.session['pk'] = sb.pk
        request.session['gheymat'] = int(sb.product.gheymat)
        request.session['total'] = sb.qnt * int(sb.product.gheymat)
        request.session['cartOnvan'] = sb.product.onvan
        request.session['desc'] = sb.product.tosif


        return redirect("/sabad")
    else:
        return redirect("/users")

def delcart(request,adad):
    if(request.session.get("login")):
        cl=User.objects.get(username=request.session["login"])
        pr=prd.objects.get(id=adad)
        sb=sabad.objects.filter(client=cl,product=pr)
        sb.delete()
        return redirect("/sabad")
    else:
        return redirect("/users")

def editqnt(request,adad):
    if(request.session["login"]):
        cl=client.objects.get(username=request.session["login"])
        pr=prd.objects.get(id=adad)
        qnt=request.POST.get("qnt")

        if not qnt:
            sb=sabad.objects.filter(client=cl,product=pr).first()
            return redirect("/sabad")
        
        sb=sabad.objects.filter(client=cl,product=pr).first()
        sb.qnt=qnt
        sb.save()
        return redirect("/sabad")
    else:
        return redirect("/users")


def vsabad(request):
    if(request.session.get("login")):
        cl=client.objects.get(username=request.session["login"])
        p=sabad.objects.filter(client=cl)
        t=0
        for m in p:
            t=t+m.product.gheymat
        return render(request,"shop/sabad.html",{"p":p,"t":t})
    else:
        return redirect("/")

        
def lout(request):
    del request.session["login"]
    return redirect("/")


def reg(request):
    if request.method=="POST":
        status=False
        context={"errors":[]}
        f=request.POST.get("fname")
        l=request.POST.get("lname")
        e=request.POST.get("email")
        u=request.POST.get("username")
        p=request.POST.get("password")
        rp=request.POST.get("rpassword")
        if len(p)<6:
            status=True
            context["errors"].append("Password must be 6 charactes")

        if p!=rp:
            status=True
            context["errors"].append("re-password is not match")

        if(status==False):

            user = client.objects.create(username=u, password=p)
            return redirect("/success")
        else:
            return render(request,"shop/reg.html",context=context)


    return render(request,"shop/reg.html")

def upanel(request):
    if request.session['login']:
        return render(request,"shop/userspanel.html")
    else:
        return redirect("/users")


def error(request):
    return render(request, "shop/error.html")


def sc(request):
    return render(request,"shop/sc.html")


def users(request):
    if (request.method=="POST"):
        u=request.POST.get("username")
        p=request.POST.get("password")
        user=client.objects.filter(username=u,password=p)
        if user:
            request.session['login'] = u
            return redirect("/userspanel")
        else:
            return redirect("/error")


    return render(request,"shop/users.html")

def buy(request,pk):
    sb = sabad.objects.get(pk=pk)
    total = int(sb.product.gheymat) * sb.qnt
    fk = faktor.objects.create(client= sb.client, totalprice= total)
    fk.save()
    fk_d = faktor_details.objects.create(faktor=fk, qnt=sb.qnt, product=sb.product)
    fk_d.save()
    fkpk=fk.pk
    print(sb.product.gheymat)
    return redirect(f"/request/{fkpk}")



 


from django.shortcuts import render
import razorpay
import json
from django.views.decorators.csrf import csrf_exempt
from razorpay.resources import payment
from .models import Donate
# Create your views here.
def index(request):
    return render(request, "index.html")

def success(request):
    return render(request,"success.html")
def donate(request):
    if request.method=="POST":
        print(request.POST)
        name=request.POST.get("name")
        amount=int(request.POST.get("amount"))*100     
        client=razorpay.Client(auth=("rzp_test_kUTeDv08xseQlC","vCGvTqNPLc1ojfTfRiznHDDH"))
        payment= client.order.create({'amount': amount,'currency':'INR','payment_capture':'1'})
        print(payment)
        coffee=Donate(name=name, amount=amount, payment_id=payment['id'])
        coffee.save()
        return render(request, "razor.html",{'name':name, 'amount':amount,'order_id':payment['id']})
    return render(request, "index1.html")


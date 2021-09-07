from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from computerstore.models import computerstore
from computerstore.form import  store
# const firebaseConfig = {
#   apiKey: "AIzaSyAJqetE313KQUguhnw_6rpT_6ZQ4I7PTdk",
#   authDomain: "location-10b50.firebaseapp.com",
#   databaseURL: "https://location-10b50-default-rtdb.firebaseio.com",
#   projectId: "location-10b50",
#   storageBucket: "location-10b50.appspot.com",
#   messagingSenderId: "254261673074",
#   appId: "1:254261673074:web:c46bc35ffcbba9c5cf16eb"
# }

def home(request):
    data=computerstore.objects.all()
    return render(request,"home1.html",{'data':data})


def add(request):
    # data=computerstore.objects.get(id=id)
    if request.method=="POST":
        form=store(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect('/home1')
    return render(request,"add.html")

def detail(request,id):
    data1=computerstore.objects.get(id=id)
    print(data1.Product_name)
    return render (request,'detail.html',{'data1':data1})
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from account.models import User
from rasberrypy.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def main(request):
    if request.session["userId"]:
        user = User.objects.get(userId=request.session["userId"])
        picture = BabyPicture.objects.get(id = 9)
        # picture = BabyPicture.objects.filter(productionKey = 1,).order_by("-createTime",)
        # if len(picture):
        #     picture = picture[0]
        babyStatus = BabySick.objects.filter(productionKey = user.productionKey).order_by("-createTime",)
        if len(babyStatus) :
            babyStatus = babyStatus[0]
        return render(request,"parent/main.html",{
            "picture" : picture,
            'babyStatus': babyStatus,
        })
    else:
        return redirect("/account/login")


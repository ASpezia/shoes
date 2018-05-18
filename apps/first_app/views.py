# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
import bcrypt

# Create your views here.
def index(request):
    return render(request, "index.html")


def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for tag, error in errors.items():
            messages.error(request, error)
            print errors
        return redirect("/")
    else:
        print "register"
        pw = request.POST["password"]
        hash1 = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        u = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"],email=request.POST["email"], password=hash1)
        #above created a user, and stored it in a variable called u
        request.session["user_id"] = u.id #stored the user id in session
        #request.session["alias"] = u.alias #stored the ailias in session
    return redirect("/shoes")

def login(request):
    errors = User.objects.login_validator(request.POST)
    print errors
    if len(errors) >0:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            print errors
        return redirect("/")
    else:
        print "login"
        user = User.objects.get(email = request.POST["email"]) #get the user based on their email. This could be any column in the User table
        request.session["user_id"] = user.id #store user id in session
        return redirect("/shoes")
    return redirect("/shoes" )

def shoes(request):
    user = User.objects.get(id = request.session['user_id'])
    shoes = Item.objects.all()
    context = {
    "shoes" : shoes,
    "user" : user
    }

    return render(request,"shoes.html", context)


def dashboard(request):
    #new_item = Item.objects.create(amount = request.POST['amount'] )
    #print new user
    user = User.objects.get(id = request.session['user_id'])
    #print user
    p = Item.objects.filter(buyer = request.session['user_id']) #Wherever buy gets set? Said josh. id should rather be a string
    print p
    item_for_sale = Item.objects.all()
    context = {
      "user" :user,
      "p" : p,
     # "new_item" : item,
      "item_for_sale" : item_for_sale
      }
    return render(request, "dashboard.html", context)

def remove(request):
    return render(request, "dashboard.html")
def sell(request):
    #new_item = Item.objects.create(product = request.POST['product'], amount = request.POST['amount'], buyer = request.session['user_id'], seller = User.objects.exclude(request.session['user_id']),date_posted = NOW(), user_selling = User.objects.get(id=id), user_buying = request.session['user_id']  )

    return redirect('/shoes')






def logoutfunc(request):
    request.session.flush()
    return redirect('/logout')


def logout(request):
    return render(request, "index.html")

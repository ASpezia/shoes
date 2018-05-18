# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import re
import bcrypt
password_regex = re.compile('^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
DATE_REGEX = re.compile(r'^[0-9]+/$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class RegManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if User.objects.filter(email = postData["email"]).exists():
            errors["email"] = "Email already exists"
        if len(postData["first_name"]) < 3:
            errors["first_name"] = " name should be more than 3 characters"
        if len(postData["last_name"]) < 3:
            errors["last_name"] = "alias should be more than 3 characters"
        if len(postData["email"]) < 3:
            errors["email"] = "Email should be more than 3 characters"
        if len(postData["password"]) < 8:
            errors["password"] = "Password should be more thatn 8 characters"
        if postData["password"] != postData["confirm_password"]:
            errors["confirm_password"] = "Password confirmation does not match"
            print errors
        return errors
    def login_validator(self, postData):
        errors = {}
        if len(postData["email"]) < 3:
            errors["email"] = "Email should be more than 3 characters"
        if len(postData["password"]) < 8:
            errors["password"] = "Password must be longer than 8 characters"
        check = User.objects.filter(email=postData["email"])
        print check
        if len(check) == 0:
            errors["email"] = "Must enter an email address"
            return errors
        if not bcrypt.checkpw(postData["password"].encode(), check[0].password.encode()):
            errors["password"] = "Password doesn't match"
        return errors
    def pw_validator(self, postData):
        errors = {}
        if len(postData["password"]) < 8:
            errors["password"] = "Password must be longer than 8 characters"
        if postData["password"] != postData["confirm_password"]:
            errors["confirm_password"] = "Password confirmation does not match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)
    email = models.CharField(max_length= 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegManager()

class Item(models.Model):
    product = models.CharField(max_length = 255)
    buyer = models.CharField(max_length = 255)
    seller = models.CharField(max_length = 255)
    date_posted = models.DateField(max_length = 255)
    amount = models.IntegerField()
    user_selling = models.ForeignKey(User, related_name = "seller_of_products")
    user_buying = models.ForeignKey(User, related_name = "buyer_of_products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

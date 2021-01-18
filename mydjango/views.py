#!/usr/bin/python3
#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    return HttpResponse("Hello World!")
def first(request):
    return HttpResponse("Hello World! first Page.")
def erro(request):
    return HttpResponse("404,Not found!")
def runoob(request):
    context = {}
    context["hello"] = "helo"
    return render(request,'runoob.html',context)
def score(request):
    score = 88
    return render(request,'score.html',{"num":score})
def tags(request):
    return render(request,'tags.html')

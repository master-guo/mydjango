#!/usr/bin/python3
#coding:utf-8
from django import template

register = template.Library()

@register.simple_tag
def my_tag1(v1, v2, v3):
    return v1 * v2 * v3

@register.filter
def my_filter(v1, v2):
    return v1 * v2
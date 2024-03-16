from django.template.context_processors import request

from phones.models import Phone
from django.shortcuts import render, redirect


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_by = request.GET.get('sort', 'name')
    phone_objects = Phone.objects.all()

    if sort_by == 'max_price':
        phone_objects_sorted = phone_objects.order_by('-price')

    elif sort_by == 'min_price':
        phone_objects_sorted = phone_objects.order_by('price')

    elif sort_by == 'name':
        phone_objects_sorted = phone_objects.order_by('name')

    context = {'phones': phone_objects_sorted}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_objects = Phone.objects.filter(slug__contains=slug).first()
    context = {'phone': phone_objects}
    return render(request, template, context)

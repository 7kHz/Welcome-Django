from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, template, context)

# def show_phones(request):
#     phone_objects = Phone.objects.all()
#     phones = [f'{p.name}, {p.price}, {p.image}' for p in phone_objects]
#     return HttpResponse('<br>'.join(phones))

def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)

from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort', 0)
    if sort == 'name':
        phones = phones.order_by('name')
    elif sort == 'min_price':
        phones = phones.order_by('price')
    elif sort == 'max_price':
        phones = phones.order_by('-price')
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    context = {}
    template = 'product.html'
    phones = Phone.objects.all()
    for phone in phones:
        if phone.slug == slug:
            context_ = {'slug': slug,
                        'phone': phone}
            context.update(context_)
    return render(request, template, context)
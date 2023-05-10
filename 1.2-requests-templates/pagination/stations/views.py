from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv



def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', encoding='utf8') as csvfile:
        rows = csv.DictReader(csvfile)
        stations = [station for station in rows]
    paginator = Paginator(stations, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

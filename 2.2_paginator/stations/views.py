from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
from csv import DictReader
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    file = open(BUS_STATION_CSV, encoding="utf-8")
    csv_file = list(DictReader(file))
    paginator = Paginator(csv_file, 10)
    current_page = int(request.GET.get('page', 1))
    page = paginator.get_page(current_page)

    context = {
        'bus_stations': page,
        'page': page
    }
    return render(request, 'stations/index.html', context)

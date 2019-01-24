from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from . import forms
from .models import Station

def find_train(request):
    return render(request, 'find_train.html')

def index(request):
    return render(request, 'first_app/index.html')

def user(request):
    return render(request, 'first_app/userDashboard.html')

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def result(request):
    source = request.POST['source']
    destination = request.POST['destination']
    query = 'select src.id, src.train_id, first_app_train.train_name, src.departure_time as departure_time, dst.arrival_time as arrival_time from first_app_train INNER JOIN first_app_station as src cross join first_app_station as dst WHERE src.station_name = %s and dst.station_name = %s and src.train_id = dst.train_id and src.train_id = first_app_train.train_no and src.departure_time < dst.arrival_time;'
    # query = "SELECT * FROM first_app_station"
    # query_results = list(Station.objects.all().values('id', 'train_id', 'train_id__train_name'))
    cursor = connection.cursor()
    cursor.execute(query, (source, destination))
    query_results = dictfetchall(cursor)
    context = {'query_results' : query_results}
    return render(request, 'result.html', context)

def Register_view(request):
    form = forms.Register()

    if request.method == 'POST':
        form = forms.Register(request.POST)

        if form.is_valid():
            #do some code
            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("USERNAME: " + form.cleaned_data['username'])
            print("PASSWORD: " + form.cleaned_data['password'])
            print("VARIFY_PASSWORD: " + form.cleaned_data['varify_password'])




    return render(request, 'first_app/form_page.html', {'form':form})

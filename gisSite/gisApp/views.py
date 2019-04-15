from django.shortcuts import render
from django.http import HttpResponse

def login(request):
	return render(request, 'gisApp/login.html')

# def home(request):
# 	return render(request, 'gisApp/index.html')

def home(request):
	return render(request, 'gisApp/index.html', {'title':'Home'})

def subcounty_datasets(request):
    subcounties = serialize('geojson' , Subcounties.objects.all())
    return HttpResponse(subcounties, content_type= 'json')

def ngo_projects_datasets(request):
    ngoprojs = serialize('geojson' , Ngoprojs.objects.all())
    return HttpResponse(ngoprojs, content_type= 'json')

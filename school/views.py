from django.shortcuts import render, HttpResponse
from py2neo import Graph
# Create your views here.



def save_data(request):
    graph = Graph(**settings.NEO4J_DATABASES['default'])
    # data = request.POST.get('data')
    data = "Ndolo"
    graph.run("CREATE (:Label {data: {data}})", data=data)
    return HttpResponse("Data saved successfully.")
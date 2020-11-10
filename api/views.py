from django.shortcuts import render
from django.http import JsonResponse

from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

# Create your views here.

@api_view(['GET'])#@api_view decorator for working with function based views.
def apiOverview(request):
    api_urls = {
        'List':'/task-list',
        'Detail View':'task-detail/<str:pk>/',
        'Create':'task-create/',
        'Update':'task-update/<str:pk>/',
        'Delete':'task-delete/<str:pk>/',
    }
    #changed it to a django rest framwrok resplonse
     #return JsonResponse("API BASE POINT", safe=False)
     
    return Response(api_urls)
   
@api_view(['GET'])#@api_view decorator for working with function based views.
def taskList(request):
    tasks = Task.objects.all()#quering the database
    # we have put object tasks into the serializer
    #many = True -->> serializes a list of objects
    #many = False -->> serializes a one object
    serializer = TaskSerializer(tasks, many=True)#serializing the data
    return Response(serializer.data)# returns the data in api response

@api_view(['GET'])#@api_view decorator for working with function based views.
def taskDetail(request, pk):
    tasks = Task.objects.get(id = pk)#quering the database for a single item
    serializer = TaskSerializer(tasks, many=False)#serializing the data
    return Response(serializer.data)# returns the data in api response


@api_view(['POST'])#@api_view decorator for working with function based views.
def taskCreate(request):
    #request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.
    serializer = TaskSerializer(data = request.data)#serializing the data
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)# returns the data in api response

@api_view(['POST'])#@api_view decorator for working with function based views.
def taskUpdate(request, pk):
    task = Task.objects.get(id = pk)
    #request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.
    serializer = TaskSerializer( instance=task, data = request.data)#serializing the data
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)# returns the data in api response


@api_view(['DELETE'])#@api_view decorator for working with function based views.
def taskDelete(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return Response('Item Successfully Deleted')# returns the data in api response
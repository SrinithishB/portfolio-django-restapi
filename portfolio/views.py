from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def project_list(request):
    if request.method=="GET":
        projects=Projects.objects.all()
        serializer=ProjectSerializers(projects,many=True)
        return  JsonResponse({'projects':serializer.data})
    if request.method=="POST":
        serializer=ProjectSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
def project_detail(request,id):
    try:
        project=Projects.objects.get(pk=id)
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=ProjectSerializers(project)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer=ProjectSerializers(project,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
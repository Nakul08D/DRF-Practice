from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import CourseSerializers
from .models import Course
from rest_framework.parsers import JSONParser
import io
# Create your views here.

@api_view(['GET','POST'])
def course_view(request):
    if request.method=='GET':
        course=Course.objects.all()
        serializer=CourseSerializers(course, many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=CourseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    # elif request.method=='PATCH':
    #     json_data=request.body
    #     stream=io.BytesIO(json_data)
    #     python_data=JSONParser().parse(stream)
    #     id=python_data.get('id')
    #     print('============',id)
    #     course=Course.objects.get(id=id)
    #     serializer=CourseSerializers(course, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status.HTTP_304_NOT_MODIFIED)

@api_view(['GET','DELETE','PUT','PATCH'])
def course_view_id(request,id):
    try:
        course=Course.objects.get(id=id)
    except course.DoesNotExit:
        return Response(status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=CourseSerializers(course)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=CourseSerializers(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status.HTTP_304_NOT_MODIFIED)
        
    elif request.method=='PATCH':
        serializer=CourseSerializers(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status.HTTP_304_NOT_MODIFIED)
    
    elif request.method=='DELETE':
        course.delete()
        return Response(status.HTTP_200_OK)
            
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer,AddStudentSerializer
from .models import Student,AddStudent
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
# Create your views here.

def home(request):
    student=Student.objects.all()
    serializer=StudentSerializer(student,many=True)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def info(request,id=None):
    if request.method=="GET":
        if id != None:
            st=AddStudent.objects.get(id=id)
        else:
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            id=python_data.get('id')
            st=AddStudent.objects.get(id=id)
        if id is not None:
            serializer=AddStudentSerializer(st)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        else:
            serializer=AddStudentSerializer(st,many=True)
            # json_data=JSONRenderer().render(st)
            # return HttpResponse(json_data,content_type='application/json')
            return JsonResponse(serializer.data,safe=False)
                
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        print("===========",python_data)
        serializer=AddStudentSerializer(data=python_data)
        
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Saved'}
            data=JSONRenderer().render(res)
            return HttpResponse(data,content_type='application/json')
            # return JsonResponse(serializer.data,safe=False)
        else:
            data=JSONRenderer().render(serializer.errors)
            return HttpResponse(data,content_type='application/json')

        
    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        st=AddStudent.objects.get(id=id)
        #partial used for partial update
        serializer=AddStudentSerializer(st,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Updated'}
            data=JSONRenderer().render(msg)
            return HttpResponse(data,content_type='application')
        else:
             data=JSONRenderer().render(serializer.errors)
             return HttpResponse(data,content_type='application/json')
        
    if request.method=="DELETE":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        st=AddStudent.objects.get(id=id)
        st.delete()
        msg={'del':'Deleted'}
        data=JSONRenderer().render(msg)
        return HttpResponse(data,content_type='application')
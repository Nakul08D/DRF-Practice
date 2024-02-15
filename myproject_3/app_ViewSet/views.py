from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.viewsets import ViewSet , ModelViewSet
from rest_framework.response import Response


# ModelViewSet:
class StudentViewSet(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


'''
# ViewSet:
class StudentViewSet(ViewSet):
    
    def list(self, request):
        student=Student.objects.all()
        serializer=StudentSerializer(student, many=True)
        return Response(serializer.data)
    
    
    def retrieve(self, request, pk):
        try:
            student=Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer=StudentSerializer(student)
        return Response(serializer.data)
    
    def create(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk):
        try:
            student=Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)  
        serializer=StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(status.HTTP_304_NOT_MODIFIED)
        
    def destroy(self, request, pk):
        student=Student.objects.get(pk=pk)
        student.delete()
        return Response(status.HTTP_200_OK)
'''
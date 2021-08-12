from django.shortcuts import render
from Student.models import *
from Student.serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class StudentApi(APIView):
    def get(self, req, pk=None):
        if pk is not None:
            _student = student.objects.get(id=pk)
            serializer = StudentSerializer(_student)
            return Response(serializer.data)

        _student = student.objects.all()
        serializer = StudentSerializer(_student,many=True)
        return Response(serializer.data)

    def post(self, req):
        print(req.data)
        serializer = StudentSerializer(data = req.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"success"})
        else:
            return Response(serializer.errors)

    def put(self, req, pk):
        _student = student.objects.get(id=pk)
        serializer = StudentSerializer(_student, data = req.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"success"})
        else:
            return Response(serializer.errors)

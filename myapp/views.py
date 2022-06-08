from http.client import responses
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json
from .models import Student, Course
from .serializers.cource_serializer import CourseSerializer
from .serializers.student_serializer import StudentSerializer

# Create your views here.

class CourseAPIView(APIView):
    model_class = Course.objects
    
    def get_objet(self, pk):
        try:
            return self.model_class.get(pk=pk)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)

    def get(self,request, *args, **kwargs):
        courses = self.model_class.all()
        list_data = list() 
        for cource in courses:
            data = self.transfor_single(cource)
            if data:
                list_data.append(data)

        return Response(list_data)                


    def post(self, request, *args, **kwargs):
        data = request.data.copy()

        serializer = CourseSerializer(data = data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        cource = self.get_objet(pk = pk)
        if cource:
            cource.delete()
            return Response(status =status.HTTP_200_OK)
        return Response(status =status.HTTP_204_NO_CONTENT)

    def transfor_single(self, instance):
        resp_dict = dict()

        resp_dict["id"] = instance.id
        resp_dict["name"] = instance.name
        resp_dict["prof_name"] = instance.prof_name
        resp_dict["description"] = instance.description

        return resp_dict


class StudentAPIView(APIView):
    model_class = Student.objects.select_related('course')
    
    def get_objet(self, pk):
        try:
            return self.model_class.get(pk=pk)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)

    def get(self,request, *args, **kwargs):
        students = self.model_class.all()
        list_data = list() 
        for studnet in students:
            data = self.transfor_single(studnet)
            if data:
                list_data.append(data)

        return Response(list_data)                


    def post(self, request, *args, **kwargs):
        data = request.data.copy()

        course_id = data.get("course")
        
        if not course_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
 
        course_instance = Course.objects.filter(id=course_id).first()
        
        if not course_instance:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = StudentSerializer(data = data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    

    def transfor_single(self, instance):
        resp_dict = dict()

        resp_dict["id"] = instance.id
        resp_dict["name"] = instance.name
        resp_dict["email"] = instance.email
        resp_dict["phone"] = instance.phone

        resp_dict["cource_id"] = instance.course_id
            # resp_dict["cource_name"] = instance.course.name

        return resp_dict
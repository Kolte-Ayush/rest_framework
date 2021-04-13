from pprint import pprint

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
from django.http import Http404


class CollegeList(APIView):
    """
       List all snippets, or create a new snippet.
       """

    def get(self, request, search):
        if len(search) > 0:
            return self.search_college(self, search)
        snippets = College.objects.all()
        serializer = CollegeSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {
                    "collegeName": [
                        "This College Name is required."
                    ],
                    "collegeAddress": [
                        "This College Address is required."
                    ],
                    "collegeState": [
                        "This College State is required."
                    ],
                    "collegeCity": [
                        "This College City is required."
                    ],
                    "collegePhoneNumber": [
                        "This Phone Number is required."
                    ]}, status=status.HTTP_400_BAD_REQUEST)

    def search_college(self, request, param):
        query = College.objects.filter(collegeName__icontains=param)
        if len(query) > 0:
            serializer = CollegeSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("No Data Found", status=status.HTTP_204_NO_CONTENT)


class CollegeUpdate(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return College.objects.get(pk=pk)
        except College.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CollegeSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CollegeSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                {
                    "collegeName": [
                        "This College Name is required."
                    ],
                    "collegeAddress": [
                        "This College Address is required."
                    ],
                    "collegeState": [
                        "This College State is required."
                    ],
                    "collegeCity": [
                        "This College City is required."
                    ],
                    "collegePhoneNumber": [
                        "This Phone Number is required."
                    ]}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print("delete function call")
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseCtl(APIView):

    def get(self, request, pk=0, search=[]):
        if len(search) > 0:
            return self.search_course(self, search)
        else:
            if pk > 0:
                query = Course.objects.filter(id=pk)
                serializer = CourseSerializer(query, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                query = Course.objects.all()
                if len(query) > 0:
                    serializer = CourseSerializer(query, many=True)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response("No data Found")

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        snippet = Course.objects.get(pk=pk)
        serializer = CourseSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            snippet = Course.objects.get(pk=pk)
            snippet.delete()
            return Response("Successfully Deleted", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("Object is Deleted OR Object is Not found")

    def search_course(self, request, param):
        query = Course.objects.filter(courseName__icontains=param)
        if len(query) > 0:
            serializer = CourseSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("No Data Found", status=status.HTTP_204_NO_CONTENT)


class StudentView(APIView):

    def get(self, request, pk=0):
        if pk > 0:
            query = Student.objects.filter(id=pk)
            serializer = StudentSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            query = Student.objects.all()
            if len(query) > 0:
                serializer = StudentSerializer(query, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("No data Found")

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        snippet = Student.objects.get(pk=pk)
        serializer = StudentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            snippet = Student.objects.get(pk=pk)
            snippet.delete()
            return Response("Successfully Deleted", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("Object is Deleted OR Object is Not found")


class SubjectView(APIView):

    def get(self, request, pk=0):
        if pk > 0:
            query = Subject.objects.filter(id=pk)
            serializer = SubjectSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            query = Subject.objects.all()
            if len(query) > 0:
                serializer = SubjectSerializer(query, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("No data Found")

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        snippet = Subject.objects.get(pk=pk)
        serializer = SubjectSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            snippet = Subject.objects.get(pk=pk)
            snippet.delete()
            return Response("Successfully Deleted", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("Object is Deleted OR Object is Not found")

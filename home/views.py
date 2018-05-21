# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from models import books
import uuid

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from models import books
from serializers import HomeBooksSerializer
from rest_framework import generics
from rest_framework import viewsets
from django.conf.urls import url

class BookViewSet(viewsets.ModelViewSet):
    queryset = books.objects.all()
    serializer_class = HomeBooksSerializer


def index(request):
    # for i in range(11,20):
    #     tmp_uuid = uuid.uuid4()
    #     return_uuid = str(tmp_uuid).replace("-", "")
    #     books_uuid = return_uuid
    #     name = 'shijianjianshi'+ str(i)
    #     introduction = 'jianjie'+ str(i)
    #     author='woshizuozhe' + str(i)
    #     comment = '我排位排位排位' + str(i)
    #     tmp_uuid1 = uuid.uuid4()
    #     return_uuid1 = str(tmp_uuid1).replace("-", "")
    #     photo = return_uuid1
    #     books.objects.create(uuid=books_uuid,name=name,introduction=introduction,author=author,comment=comment,photo=photo)

    return HttpResponse('<h1>hello,django</h1>')

class BookBaseList(APIView):
    def get(self,request,format = None):
        book = books.objects.all()
        serializer = HomeBooksSerializer(book, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = HomeBooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BookBaseCreate(generics.ListCreateAPIView):
    queryset = books.objects.all()
    serializer_class = HomeBooksSerializer

class BookBaseDetail(generics.ListCreateAPIView):
    serializer_class = HomeBooksSerializer

    def get(self,request,*args,**kwargs):
        book = books.objects.get(pk=kwargs['pk'])
        serializer = HomeBooksSerializer(book)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        serializer = HomeBooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def book_detail(request,pk):
    try:
        book = books.objects.get(pk = pk)
    except Exception as e:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HomeBooksSerializer(book)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = HomeBooksSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
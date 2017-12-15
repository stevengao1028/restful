# coding=utf-8
from django.shortcuts import render
import json

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apitest.models import profit,person
from apitest.serializer import profitSerializer, personSerializer
from django.views.decorators.csrf import ensure_csrf_cookie


def home(request):
    return render(request,'machine/index.html')

@api_view(['GET', 'PUT'])
# @csrf_exempt
def profit_list(request):
    """
    显示profit所有数据,后者创建一个新的snippet
    """
    # try:
    #     profits = profit.objects.filter(stk_code=request.data)
    # except profit.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        profits = profit.objects.all()
        serializer = profitSerializer(profits, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # print request.data['stk_code']
        serializer = profitSerializer(data=request.data)
        print serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def person_lists(request):
    """
    显示profit所有数据,后者创建一个新的snippet
    """
    if request.method == 'GET':
        persons = person.objects.all()
        serializer = personSerializer(persons, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        print str(request.data)
        serializer = personSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



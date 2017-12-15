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

def home(request):
    return render(request,'machine/index.html')

@api_view(['GET', 'POST'])
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
    elif request.method == 'POST':
        print request.POST['searchtext']
        # searchtext = request.data['searchtext']
        # print searchtext
        # serializer = profitSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        profits = profit.objects.all()
        serializer = profitSerializer(profits, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def person_lists(request):
    """
    显示profit所有数据,后者创建一个新的snippet
    """
    if request.method == 'GET':
        persons = person.objects.all()
        serializer = personSerializer(persons, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print str(request.data)
        serializer = personSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


